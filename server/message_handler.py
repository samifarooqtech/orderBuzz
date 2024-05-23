from flask import Flask, jsonify

def get_message():
    message = "This is a message from the Flask backend!"
    return jsonify({'message': message})
