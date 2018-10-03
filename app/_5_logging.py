import logging
from flask import Flask

app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.basicConfig(
    filename="mytest.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )


# SAMPLE 1 - logging
# http://127.0.0.1:5000/logme
# output is  : DEBUG:root:Logged : first log
@app.route('/logme')
def logme():
    logging.debug("Logged : {} {}".format('first', 'log'))
    return 'Logged'