from flask import Flask, request
import africastalking

app = Flask(__name__)

# Initialize Africa's Talking SDK
username = "Davie.Muigai"
api_key = "9117144113c92aa72fb559f2a1406d47b6ad9df881398354bd841143c06c7fcb"
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
        # This is the first request. Note how we start the response with CON
        response = "CON Welcome to Sokokoa \n"
        response += "1. Get started \n"
        response += "2. Already a member \n"
        response += "3.  Company info "
    else:
        # Split the text to get the menu level
        text_array = text.split('*')
        user_response = text_array[-1]

        if user_response == "1":
            response = "CON Registartion  \n"
            response += "1. Id NO \n"
            response += "2. Phone Number\n"
            response += "3. Product \n"
            response += "4. Region "
       # elif text          == '1*1':
      # This is a second level response where the user selected 1 in the first instance
        # response += "2. Seller\n"
      # This is a terminal request. Note how we start the response with END
   



        elif user_response == "2":
            response = "CON You have selected Option 2 \n"
            response += "1. Buyer\n"
            response += "2. Seller\n"
            # response += "3.  Company info "


        elif user_response == "3":
            response = "CON You have selected Option 3\n"
            response += "1. About us \n"
            response += "2. Contact us \n"
            response += "3.  Location "

        elif user_response  == "1*1":
            response = "CON You have selected Option 3\n"
            response += "1. jhjsdfk \n"
            response += "2. Conterwgus \n"
            response += "3.  Locat32rt5t43t "  

        else:
            response = "END Invalid option. Please try again."

    return response

   



if __name__ == '__main__':
      app.run(debug=True)
