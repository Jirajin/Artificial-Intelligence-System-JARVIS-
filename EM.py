import time
import config
import send_email
from speak import Say
from listen import Listen

EMAIL_DIC = {
    'myself': 'jirajin43@gmail.com',
    'my official email': 'atharvaaingle@gmail.com',
    'my official mail': 'atharvaaingle@gmail.com',
    'my second email': 'sihitishiti@gmail.com'
}


def send_mail(sender_email, sender_password, receiver_email, msg):
    return send_email.mail(sender_email, sender_password, receiver_email, msg)


def Email():
    sender_email = config.email
    sender_password = config.email_password

    try:
        Say("Whom do you want to email sir ?")
        recipient = Listen()
        receiver_email = EMAIL_DIC.get(recipient)
        if receiver_email:

            Say("What is the subject sir ?")
            subject = Listen()
            Say("What should I say?")
            message = Listen()
            msg = 'Subject: {}\n\n{}'.format(subject, message)
            send_mail(sender_email, sender_password,
                      receiver_email, msg)
            Say("Email has been successfully sent")
            time.sleep(2)

        else:
            Say(
                "I coudn't find the requested person's email in my database. Please try again with a different name")

    except:
        Say("Sorry sir. Couldn't send your mail. Please try again")


Email()
