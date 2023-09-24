from flask import Flask,request
import receipt_processor as rp

app = Flask(__name__)

@app.post("/receipts/process")
def process_receipt():
    return rs.process_receipt(request)
@app.get("/receipts/{id}/points")
def get_points(id):
    return rs.get_points(id)