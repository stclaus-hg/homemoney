class Methods:
    GET = 'GET'
    POST = 'POST'


CSRF_ENABLED = True
SECRET_KEY = "Xigie1uu Doh1eixe aeZai6Oh kohz4Vah Okia7eij Yaequee3 Ath5curo roh4OhG4"
SQLALCHEMY_DATABASE_URI = 'sqlite:///homemoney.db'

try:
    from config_dev import *
except:
    pass
