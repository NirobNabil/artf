from flask import *
from flask_cors import CORS
import os
import datetime
import json
import sqlite3
import base64
import random
import string
from flask import send_from_directory
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Directory to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'artf'


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
                productName TEXT NOT NULL,
                productId TEXT,
                height TEXT,
                width TEXT,
                thumbnail TEXT,
                username TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                token TEXT,
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


@app.route('/fileupload', methods=['POST'])
def file_upload():
    product_name = request.form.get('productName')

    token = request.headers.get('Authorization')
    # print(token)
    username = get_username_from_token(token)
    if not username:
        return jsonify({'error': 'Invalid token'}), 401

    product_height = request.form.get('height')
    product_width = request.form.get('width')
    product_id = str(uuid.uuid4())

    if product_name:
        # Create a directory with product name and current date-time
        product_directory = f"uploads/{product_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}/"
        os.makedirs(product_directory, exist_ok=True)

        # Save thumbnail image
        thumbnail = request.files.get('thumbnail')
        if thumbnail:
            print(thumbnail)
            thumbnail_filename = product_id + "_thumbnail." + thumbnail.filename.split('.')[-1]

            # Create a copy of the thumbnail image in static directory
            static_thumbnail_path = os.path.join(
                'static', 'uploads', thumbnail_filename)
            os.makedirs(os.path.dirname(static_thumbnail_path), exist_ok=True)
            thumbnail.save(static_thumbnail_path)

            # Construct URL for the static thumbnail image
            thumbnail_url = url_for('static', filename=os.path.join(
                'uploads', thumbnail_filename))
            print(thumbnail_url)

        # Save multiple images and their details
        images_data = []
        for i in range(1, len(request.files) + 1):
            image = request.files.get(f'image-{i}')
            if image:
                image_filename = f"sample-{i}." + image.filename.split('.')[-1]
                image.save(os.path.join(product_directory, image_filename))
                images_data.append({'filename': image_filename})

        # Convert images_data to JSON string
        images_json = json.dumps(images_data)

        # Save the product details as JSON file
        product_details = {
            'product_id': product_id,
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
            INSERT INTO products (productName, uid, height, width, thumbnail, username)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (product_name, product_directory, product_height, product_width, thumbnail_url, username))
        # Commit changes to database
        db.commit()
        print("jhsd")
        return jsonify({'message': 'Product images and details uploaded successfully', 'product_id': product_id, 'images': images_data})
    else:
        return jsonify({'error': 'Product name not provided'}), 400

# Route to retrieve product list


@app.route('/products', methods=['GET'])
def list_products():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    # Convert BLOB data to base64 encoded strings and construct product details
    products_serializable = []
    for product in products:
        product_dict = dict(product)
        # Assuming the thumbnail URL is already stored in the database
        thumbnail_url = product_dict['thumbnail']
        product_details = {
            'productName': product_dict['productName'],
            # Assuming 'uid' contains the unique identifier for each product
            'id': product_dict['productId'],
            'height': product_dict['height'],
            'width': product_dict['width'],
            'thumbnail': thumbnail_url
        }
        print(product_details)
        products_serializable.append(product_details)

    return products_serializable

    # Render the frontend using the provided .tsx file and pass product details
    # return render_template('frontend/src/pages/buyer/[id].tsx', products=products_serializable)


# Route to retrieve product details


@app.route('/product/<string:product_id>', methods=['GET'])
def product_details(product_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products WHERE productId = ?', (product_id,))
    product = cursor.fetchone()
    if product:
        return jsonify({
            'id': product['productId'],
            'productName': product['productName'],
            'height': product['height'],
            'width': product['width'],
            'thumbnail': product['thumbnail']
        })
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/list_products')
def render_list_products():
    return render_template('list_products.html')


@app.route('/product_details/<int:product_id>')
def render_product_details(product_id):
    return render_template('product_details.html', product_id=product_id)


@app.route('/product_thumbnail/<path:path>')
def serve_thumbnail(path):
    return send_from_directory(app.static_folder, path)


# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    hashed_password = generate_password_hash(password)
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400

# Route for user login


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user and check_password_hash(user['password'], password):
        # Generate token
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
        # Save token in the database
        cursor.execute(
            "UPDATE users SET token=? WHERE username=?", (token, username))
        db.commit()
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid username or password'}), 401


# Token required decorator


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'error': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated


# Function to get username from token
def get_username_from_token(token):
    try:
        # print(token)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE token=?", (token,))
        user = cursor.fetchone()
        if user:
            # print("asas"+user['username'])
            return user['username']
        else:
            # print("weee")
            return None
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Protected route example


@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'This is a protected route'})

# Route to display all products with their details listed with the username from the token


@app.route('/all_products', methods=['GET'])
# @token_required
def all_products():
    token = request.headers.get('Authorization')
    username = get_username_from_token(token)
    if not username:
        return jsonify({'error': 'Invalid token'}), 401

    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products WHERE username=?', (username,))
    products = cursor.fetchall()

    products_list = []
    for product in products:
        product_dict = dict(product)
        product_details = {
            'productName': product_dict['productName'],
            'height': product_dict['height'],
            'width': product_dict['width'],
            'thumbnail': product_dict['thumbnail']
        }
        products_list.append(product_details)

    return jsonify({'username': username, 'products': products_list})


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8080)
