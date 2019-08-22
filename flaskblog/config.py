import os


class Config:
    # Inorder to configure a db on local file system
    SECRET_KEY='e655678b14a2f3188726745220ac7ea69740871e41db707c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_PASSWORD = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')