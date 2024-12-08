import africastalking
import os
# Initialize Africa's Talking
username = "sandbox"  
api_key = os.environ.get('api_key')

africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(recipient, message):
    try:
        response = sms.send(
            message=message,
            recipients=[recipient]
        )
        print(f"SMS sent successfully: {response}")
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None
