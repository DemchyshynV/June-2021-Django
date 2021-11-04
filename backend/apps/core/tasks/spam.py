from settings.celery import app
from utils.email_utils import EmailUtils


@app.task
def email_spam():
    EmailUtils.email_spam()
