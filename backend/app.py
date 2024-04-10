from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import datetime
import json

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', file_upload_url='/fileupload')


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

        return jsonify({'message': 'Product images and details uploaded successfully', 'product_directory': product_directory, 'images': images_data})
    else:
        return jsonify({'error': 'Product name not provided'}), 400


if __name__ == "__main__":
    app.run(debug=True, port=8080)
