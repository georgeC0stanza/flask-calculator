# app.py
from flask import Flask, request, jsonify, render_template
import calc
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)
      
@app.route('/add', methods=['GET'])
def add():
    number1 = request.args.get("number1", None)
    number2 = request.args.get("number2", None)
    response = {}

    if not number1 or not number2:
        response["ERROR"] = "please send two numbers."
    else:
        result = calc.addition(int(number1), int(number2))
        response["MESSAGE"] = f"{number1} + {number2}"
        response["RESULTBINARY"] = f"{result[1]}"
        response["RESULTDECIMAL"] = f"{result[0]}"

    return jsonify(response)
    
@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/calc/')
def calculator():
    return render_template('index2.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)