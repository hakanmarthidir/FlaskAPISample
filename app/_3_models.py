import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from config import Config


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.ConnectionString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SqlAlchemyTrackModifications

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SchoolTeam(db.Model):
    __tablename__ = 'schoolteams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    students = db.relationship('Student', backref='schoolteams', lazy='select')

    # def __repr__(self):
    #     return '<SchoolTeam %r>' % self.name

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(64), unique=True, index=True)
    studentlastname = db.Column(db.String(64), index=True)
    studentage = db.Column(db.Integer, index=True)
    team_id = db.Column(db.Integer, db.ForeignKey('schoolteams.id'))

    def to_json(self):
        json_student = {
            'id': self.id,
            'studentname': self.studentname,
            'studentlastname' : self.studentlastname
        }
        return json_student


db.create_all()
print('all models were created')