import receipt_processor as rp
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.post("/receipts/process")
def process_receipt():
    return rp.process_receipt(request)
@app.get("/receipts/{id}/points")
def get_points(id):
    return rp.get_points(id)