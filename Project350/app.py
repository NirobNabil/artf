from flask import Flask, render_template, request
from flask_cors import CORS
import io
import os
app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    # elif request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     if username == 'Ayesha' and password == 'password':
    #         return "success"
    #     else:
    #         return "failure"


@app.route('/fileupload', methods=['POST'])
def file_upload():
    files = request.files.to_dict(flat=False)
    for filename in files.keys():
        files[filename][0].save("test/"+filename)
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=8080)
