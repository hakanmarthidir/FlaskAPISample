import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from app._3_models import SchoolTeam, Student
from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.ConnectionString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SqlAlchemyTrackModifications
db = SQLAlchemy(app)


@app.route('/addteam/<string:tname>')
def addteam(tname=""):
    team1 = SchoolTeam(name=tname)
    db.session.add(team1)
    db.session.commit()
    return 'OK'


@app.route('/addstudent/<string:sname>/<string:tname>')
def addstudent(sname, tname):
    team = SchoolTeam(name=tname)
    student = Student(studentname=sname, schoolteams=team)
    db.session.add(team)
    db.session.add(student)
    db.session.commit()
    return 'OK'

@app.route('/updatestudent/<int:tid>')
def updatestudent(tid):
    student = db.session.query(Student).filter(Student.team_id==tid).first()
    student.studentname = 'michael'
    db.session.add(student)
    db.session.commit()
    return 'OK'

@app.route('/deletestudent/<int:sid>')
def deletestudent(sid):
    student = db.session.query(Student).filter(Student.id==sid).first()
    db.session.delete(student)
    db.session.commit()
    return 'OK'

@app.route('/getstudents')
def getstudents():
    students = Student.query.all()
    print(students)
    return 'OK'

@app.route('/getstudentsbyteam/<int:teamid>')
def getstudentsbyteam(teamid):
    students = Student.query.filter_by(team_id=teamid).all()
    student = Student.query.filter_by(team_id=teamid).first()
    print(str(Student.query.filter_by(team_id=teamid)))
    print(students)
    print(student)
    print(student.schoolteams)
    restValues = jsonify({
        'students': [std.to_json() for std in students]
    })

    restValue = jsonify(student.to_json())
    return restValue
    # return restValue




