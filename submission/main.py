from flask import Flask,request
import receipt_processor as rp

@app.post("/receipts/process")
def process_receipt():
    return "a process"
@app.get("/receipts/{id}/points")
def get_points(id):
    return "some points"