from flask import Flask, request, jsonify

app = Flask(__name__)


# SAMPLE 1 - first
# http://127.0.0.1:5000/
@app.route('/')
def firstsample():
    return 'Flask is alive!'


# SAMPLE 2 - dynamic and multi route
# http://127.0.0.1:5000/sayhi
# http://127.0.0.1:5000/sayhi/hakan
@app.route('/sayhi/')
@app.route('/sayhi/<string:name>')
def secondsample(name=""):
    return 'sayhi ' + name


# SAMPLE 3 - Dynamic and Methods
# http://127.0.0.1:5000/hi/hakan
@app.route('/getpost/<string:name>', methods=['GET', 'POST'])
def thirdsample(name):
    if request.method == 'POST':
        return 'post ' + name
    else:
        return 'get ' + name


# SAMPLE 4 - Multi Parameters
# http://127.0.0.1:5000/multiparam/hakan/3424
@app.route('/multiparam/<name>/<int:age>', methods=['GET'])
def fourthsample(name, age):
    return 'multi parameters {} {}'.format(name, age)


# SAMPLE 5 - Multi Args
# http://127.0.0.1:5000/multi?name=hakan&age=3424
@app.route('/qstring', methods=['GET'])
def fifthsample():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'multi parameters {} {}'.format(name, age)

#post json
@app.route('/jsonstring', methods=['POST'])
def fifthjsonsample():
    name = request.get_json().get('name', '')
    print(name)
    return jsonify(request.get_json())


# SAMPLE 6 with Html
# http://127.0.0.1:5000/kocsistem
# #Notice : open url with browser and see the html.
@app.route('/reqhtml', methods=['GET'])
def kocsistem():
    return """<h1>KocSistem</h1><a href="http://www.kocsistem.com.tr">Click</a> """

#SAMPLE 7 with request header
#http://127.0.0.1:5000/useragent
#u can learn browser info
@app.route('/useragent')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

#SAMPLE 8 - app route alternative way
#http://127.0.0.1:5000/alternative
# url, endpoint name, functionname
def alternative():
    return '<h1>alternative declaration!</h1>'

app.add_url_rule('/alternative', 'alternative', alternative)


#SAMPLE 9 - Bad Request
#http://127.0.0.1:5000/badreq
# console result is "GET /badreq HTTP/1.1" 400 -
@app.route('/badreq')
def badreq():
    return '<h1>Bad Request</h1>', 400

#Show all url maps
print(app.url_map)