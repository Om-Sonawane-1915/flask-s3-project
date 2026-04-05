from flask import Flask, request, render_template_string
import boto3
import os

app = Flask(__name__)

# S3 configuration
BUCKET_NAME = "amzn-s3b-1915"

s3 = boto3.client("s3")

# UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>S3 Upload</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            text-align: center;
            padding-top: 50px;
        }

        h2 {
            color: white;
        }

        form {
            margin: 20px auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            width: 300px;
            box-shadow: 0px 0px 10px gray;
        }

        input[type="file"] {
            margin: 10px 0;
        }

        button {
            padding: 10px 20px;
            background-color: #4facfe;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #007bff;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            color: white;
            text-decoration: none;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <h2>Upload File to S3</h2>

    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file"><br>
        <button type="submit">Upload</button>
    </form>

    <a href="/files">View Files</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file:
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        return f"Uploaded {file.filename} successfully!"
    return "No file selected"

@app.route("/files")
def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    files = response.get("Contents", [])

    file_list = "<h2>Files in S3</h2><ul>"
    for f in files:
        file_list += f"<li>{f['Key']}</li>"
    file_list += "</ul><a href='/'>Back</a>"

    return file_list

if __name__ == "__main__":
    app.run(debug=True)
