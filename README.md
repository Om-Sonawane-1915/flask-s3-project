# Flask S3 File Upload Project

## 📌 Description
This is a Flask-based web application that allows users to:
- Upload files to AWS S3
- View uploaded files
- Delete files from S3

## 🚀 Features
- File upload to S3
- List all files in S3 bucket
- Delete files
- Simple UI

## 🛠 Technologies Used
- Python (Flask)
- AWS S3 (boto3)
- HTML & CSS

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/Om-Sonawane-1915/flask-s3-project  
cd flask-s3-project  

### 2. Create virtual environment
python3 -m venv venv  
source venv/bin/activate  

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Configure AWS
aws configure  

### 5. Run the app
python3 app.py  

### 6. Open in browser
http://127.0.0.1:5000  

## 🔐 Notes
- Do not expose AWS credentials
- Use environment variables in production

## 📌 Author
Om Sonawane
