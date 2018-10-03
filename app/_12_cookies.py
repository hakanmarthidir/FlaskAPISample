from flask import make_response, Flask, request
from app import api

# Max Age : Seconds
@api.route('/createcookie/')
def createcookie():
    cookieRes = make_response("First Cookie")
    cookieRes.set_cookie('first', 'hakan', max_age=60) # max_age = None
    return cookieRes


@api.route('/getcookie/')
def getcookie():
    cookieValue = request.cookies.get('first')
    return make_response(cookieValue)


# Max Age = 0
@api.route('/deletecookie/')
def deletecookie():
    cookieRes = make_response("Delete")
    cookieRes.set_cookie('first', 'hakan', max_age=0)
    return cookieRes

