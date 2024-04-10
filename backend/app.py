from flask import Flask, request, render_template, jsonify, g
from flask_cors import CORS
import os
import datetime
import json
import sqlite3
import random
import string


app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', file_upload_url='/fileupload')


# Database configuration
DATABASE = 'products.db'

# Initialize database


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Initialize cursor
        db.row_factory = sqlite3.Row
    return db

# Create database tables


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                height REAL,
                width REAL,
                thumbnail BLOB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
# Close database connection at the end of each request


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Route to handle file upload


# @app.route('/fileupload', methods=['POST'])
# def file_upload():
#     # Get product information from request
#     product_name = request.form.get('productName')
#     product_height = request.form.get('height')
#     product_width = request.form.get('width')
#     thumbnail = request.files.get('thumbnail')
#     images = request.files.getlist('images')

#     # Insert product information into database
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute('''
#         INSERT INTO products (name, height, width, thumbnail)
#         VALUES (?, ?, ?, ?)
#     ''', (product_name, product_height, product_width, thumbnail.read()))

#     # Commit changes to database
#     db.commit()

#     return jsonify({'message': 'Product uploaded successfully'}), 200

@app.route('/fileupload', methods=['POST'])
def file_upload():
    product_name = request.form.get('productName')
    product_height = request.form.get('height')
    product_width = request.form.get('width')

    if product_name:
        # Create a directory with product name and current date-time
        product_directory = f"uploads/{product_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}/"
        os.makedirs(product_directory, exist_ok=True)

        # Save thumbnail image
        thumbnail = request.files.get('thumbnail')
        if thumbnail:
            thumbnail_filename = thumbnail.filename
            thumbnail.save(os.path.join(product_directory, thumbnail_filename))

        # Save multiple images and their details
        images_data = []
        for i in range(1, len(request.files) + 1):
            image = request.files.get(f'image-{i}')
            if image:
                image_filename = image.filename
                image.save(os.path.join(product_directory, image_filename))
                images_data.append({'filename': image_filename})

        # Convert images_data to JSON string
        images_json = json.dumps(images_data)

        # Save the product details as JSON file
        product_details = {
            'product_name': product_name,
            'product_height': product_height,
            'product_width': product_width,
            'thumbnail': {'filename': thumbnail_filename},
            'images': images_data,
            'total_images': len(images_data)
        }
        with open(os.path.join(product_directory, 'product_details.json'), 'w') as json_file:
            json.dump(product_details, json_file)

       # Insert product information into database
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO products (name, height, width, thumbnail)
            VALUES (?, ?, ?, ?)
        ''', (product_name, product_height, product_width, thumbnail.read()))

        # Commit changes to database
        db.commit()
        return jsonify({'message': 'Product images and details uploaded successfully', 'product_directory': product_directory, 'images': images_data})
    else:
        return jsonify({'error': 'Product name not provided'}), 400

# Route to retrieve product list


@app.route('/products', methods=['GET'])
def list_products():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    return jsonify(products)

# Route to retrieve product details


@app.route('/product/<int:product_id>', methods=['GET'])
def product_details(product_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    if product:
        return jsonify({
            'id': product['id'],
            'name': product['name'],
            'height': product['height'],
            'width': product['width'],
            'thumbnail': product['thumbnail']
        })
    else:
        return jsonify({'error': 'Product not found'}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8080)
