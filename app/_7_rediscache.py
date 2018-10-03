from flask import Flask, make_response, redirect,abort, jsonify
import redis
app = Flask(__name__)

host = "flask.redis.cache.windows.net"
accesskey = "9RpD22GCkGpUYSKEyrAHNIPHPI+02Qr7MBP2QcJ8XSs="
redisclient = redis.StrictRedis(host=host, port=6380, password=accesskey, ssl=True)

nameList = ('asdsa1','asdas2','asdas3','sdfsdf4')
@app.route('/rediscache')
def rediscache():
    jdata= jsonify(nameList)
    data = redisclient.get("names")
    if data is None:
        redisclient.set("names",nameList)
        return jdata
    else:
        return data


@app.route('/deletecache/<string:name>')
def deletecache(name):
    redisclient.delete(name)
    return 'OK', 200

