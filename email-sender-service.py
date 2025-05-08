import ssl

from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL = ""  # Fixme: Enter the email you want to send from
APP_PASSWORD = ""  # Fixme: Enter the app password for the email you want to send from


@app.route("/send_email", methods=["POST"])
def send_email():
    """
    Route needs to receive a json body with the following: 'subject, 'body', 'receiver_email
    :return: Error string or EmailMessage object as string
    """
    # Parse request body
    data = request.get_json()

    # Create EmailMessage object with request body info
    email = EmailMessage()
    try:  # Returns error if subject, receiver_email, and body are not in request body
        email['From'] = EMAIL
        email['Subject'] = data['subject']
        email['To'] = data['receiver_email']
        email.set_content(data['body'])
        # Change host domain if using different email service
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(EMAIL, APP_PASSWORD)
            smtp.sendmail(EMAIL, data['receiver_email'], email.as_string())
            return f"Success, email send: \n{email.as_string()}"
    except KeyError:
        return ("Request Body Error:\nPlease ensure the subject(\'subject\'), "
                "receiver email(\'receiver_email\'), and body(\'body\') are included in the request body.")
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(port=8070, debug=True)
