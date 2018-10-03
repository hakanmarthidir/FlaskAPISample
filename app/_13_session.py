from flask import session, jsonify
from app import api



@api.route('/writesession/')
def writesession():
    session['firstsession'] = 'hakan'
    return 'OK', 200


@api.route('/getsession/')
def getsession():
    sessionValue = session.get('firstsession')
    return jsonify(sessionValue)


@api.route('/deletesession/')
def deletesession():
    session.pop('firstsession', None)
    return 'Session deleted'