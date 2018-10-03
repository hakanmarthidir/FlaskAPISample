import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask

app = Flask(__name__)

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# create logger
logger = logging.getLogger('firstlogger')
logger.setLevel(logging.DEBUG)

log_format = "%(asctime)s - %(levelname)s - %(message)s"
handler = TimedRotatingFileHandler("myloghandler.log", when="midnight", interval=1)
handler.setLevel(logging.DEBUG) #lowest severity
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)


# SAMPLE 1 - logging
# http://127.0.0.1:5000/applogme
@app.route('/applogme')
def applogme():
    logger.info("Logged : {} {}".format('first', 'log'))
    logger.warning("Logged : {} {}".format('first', 'log'))
    logger.debug("Logged : {} {}".format('first', 'log'))
    return 'Logged'