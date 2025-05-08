import ssl

from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL = ""  # Fixme: Add email that the email will be sent from
APP_PASSWORD = ""  # Fixme: Add app password for the email


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
            smtp.close()
            return f"Success, email sent:\n{email.as_string()}", 200
    except KeyError:
        return (f"Request Body Error:\nPlease ensure the subject(\'subject\'), receiver email(\'receiver_email\'), and body(\'body\') "
                f"are included in the body."), 400
    except Exception as e:
        return f"Error: {e}", 400


if __name__ == "__main__":
    app.run(port=8070, debug=True)
