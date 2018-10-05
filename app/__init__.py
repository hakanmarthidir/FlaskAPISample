from flask import Flask, Blueprint

app = Flask(__name__)
api = Blueprint('api', __name__)
app.secret_key = "my super secret key"

from . import _10_blueprint
from . import _12_cookies
from . import _13_session

app.register_blueprint(api, url_prefix='/api/v1')
app.run()