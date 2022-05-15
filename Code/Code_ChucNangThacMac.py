from flask import Flask, render_template, request, redirect
from models import db, EmployeeModel
from flask_sqlalchemy import SQLAlchemy

db = SQL_TTNTHouse()


class ThacMac_Model(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    KH_id = db.Column(db.Integer(), unique=True)
    ThacMac = db.Column(db.String())

    def __init__(self, KH_id, ThacMac):
        self.KH_id = KH_id
        self.ThacMac = ThacMac


app = Flask(__name__)

app.config['SQL_TTNTHouse_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQL_TTNTHouse_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        KH_id = request.form['KH_id']
        name = request.form['name']
        KH = ThacMac_Model(
            KH_id=KH_id, ThacMac=name)
        db.session.add(KH)
        db.session.commit()
        return ('Gửi thành công! Thắc mắc của bạn sẽ được phản hồi trong thời gian sớm nhất!')
