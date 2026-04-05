from flask import Flask, request, render_template_string
import boto3
import os

app = Flask(__name__)

# S3 configuration
BUCKET_NAME = "amzn-s3b-1915"

s3 = boto3.client("s3")

# UI
HTML_PAGE = """
<h2>Upload File to S3</h2>
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Upload</button>
</form>

<h2>Files in S3</h2>
<a href="/files">View Files</a>
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
