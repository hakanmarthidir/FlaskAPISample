from flask import Flask, make_response, redirect,abort, jsonify
import json
app = Flask(__name__)

#Sample 1 response
#http://127.0.0.1:5000/makeresponse
@app.route('/makeresponse')
def makeresponse():
    response = make_response('<h1>Make Response Sample</h1>')
    response.set_cookie('color', 'red')
    return response

#Sample 2 redirect
#http://127.0.0.1:5000/redirector
#"GET /redirector HTTP/1.1" 302
@app.route('/redirector')
def redirector():
    return redirect('http://www.kocsistem.com.tr')

#Sample 3 abort
#http://127.0.0.1:5000/abort/4  => "GET /abort/41564 HTTP/1.1" 404
#http://127.0.0.1:5000/abort/3  => "GET /abort/3 HTTP/1.1" 200
@app.route('/abort/<int:age>')
def get_user(age):
    result = age % 2
    if result == 0:
        abort(404)
    return '<h1>Result is perfect</h1>'



nameList= ('asdsa1','asdas2','asdas3','sdfsdf4')

#Sample 4 jsonify
#http://127.0.0.1:5000/jsonreturn
@app.route('/jsonreturn')
def jsonreturn():
    return jsonify(nameList)

#Sample 5 json.dumbs
#http://127.0.0.1:5000/jsondumps
@app.route('/jsondumps')
def jsondumps():
    return json.dumps(nameList)