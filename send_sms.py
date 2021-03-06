from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER


def validates_choice(user_choice):
    """Returns bool of user's choice"""

    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        return True
    elif user_choice.lower() == "no" or user_choice.lower() == "n" or user_choice.lower() == "nope":
        return False


def gets_to_number():
    """Ask user for phone number, returns it with +1 added"""

    phone_number = raw_input("What is the phone number? ")
    complete_number = "+1" + str(phone_number)
    return complete_number


def gets_message_to_send():
    """Ask user for message to send"""

    user_message = raw_input("What message do you want to send? ")
    return user_message


def send_message(to_number, to_message, ACCOUNT_SID,
                            AUTH_TOKEN, TWILIO_NUMBER):
    """Using Twilio, sends sms message"""

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
                    to=to_number,
                    from_=TWILIO_NUMBER,
                    body=to_message)

    print "Message set. Message Id: {}".format(message.sid)


def main(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER):

    print "Welcome to this Twilio API Demo"

    user_choice = raw_input("""Would you like to send a next message? """)

    validated_user_choice = validates_choice(user_choice)

    while validated_user_choice:

        to_number = gets_to_number()
        to_message = gets_message_to_send()

        send_message(to_number, to_message, ACCOUNT_SID,
                            AUTH_TOKEN, TWILIO_NUMBER)

        user_choice = raw_input("""Would you like to send another next message? """)

        validated_user_choice = validates_choice(user_choice)


if __name__ == '__main__':
    main(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER)
