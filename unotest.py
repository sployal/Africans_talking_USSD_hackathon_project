# Install necessary packages (if not already installed)
# pip install africastalking Flask

from flask import Flask, request
import africastalking

app = Flask(__name__)

# Initialize Africa's Talking SDK
username = "your_username"
api_key = "your_apikey"
africastalking.initialize(username, api_key)
ussd_service = africastalking.USSD

@app.route('/', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    response = ""

    if text == "":
        # Initial menu
        response = "CON What would you like to do?\n"
        response += "1. Option 1\n"
        response += "2. Option 2\n"
        response += "3. Option 3"
    else:
        # Process user input
        user_response = text.split('*')[-1]
        if user_response == "1":
            response = "END You selected Option 1"
            # Add logic to control LEDs here
        elif user_response == "2":
            response = "END You selected Option 2"
            # Add logic to control LEDs here
        elif user_response == "3":
            response = "END You selected Option 3"
            # Add logic to control LEDs here
        else:
            response = "END Invalid option. Please try again."

    return response

if __name__ == '__main__':
    app.run(debug=True)
