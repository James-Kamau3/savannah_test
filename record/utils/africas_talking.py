import africastalking

# Initialize Africa's Talking
username = "sandbox"  
api_key = "atsk_d5d6144d90d8ccc0214903128fd49a927e1c2454c18968b7cf5429fc40788e8ba976cad5"  

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
