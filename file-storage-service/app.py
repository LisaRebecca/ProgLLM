from flask import Flask, request, send_file, Response
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

# Initialize MinIO client
minioClient = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "files"

# Ensure the bucket exists (create if not)
if not minioClient.bucket_exists(bucket_name):
    minioClient.make_bucket(bucket_name)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = request.form['folder'] + "/" + file.filename
    try:
        minioClient.put_object(bucket_name, file_path, file, length=-1, part_size=10*1024*1024)
        return {"message": "File uploaded successfully"}, 200
    except S3Error as e:
        return {"error": str(e)}, 500

@app.route('/list', methods=['GET'])
def list_files():
    folder = request.args.get('folder')
    files = minioClient.list_objects(bucket_name, prefix=folder, recursive=True)
    return {"files": [file.object_name for file in files]}, 200

@app.route('/read/<path:file_path>', methods=['GET'])
def read_file(file_path):
    try:
        response = minioClient.get_object(bucket_name, file_path)
        return Response(response, content_type='text/plain; charset=utf-8')
    except S3Error as e:
        return {"error": str(e)}, 500

@app.route('/download/<path:file_path>', methods=['GET'])
def download_file(file_path):
    try:
        response = minioClient.get_object(bucket_name, file_path)
        return send_file(response, attachment_filename=os.path.basename(file_path))
    except S3Error as e:
        return {"error": str(e)}, 500

@app.route('/delete/<path:file_path>', methods=['DELETE'])
def delete_file(file_path):
    try:
        minioClient.remove_object(bucket_name, file_path)
        return {"message": "File deleted successfully"}, 200
    except S3Error as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=34568)