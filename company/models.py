from company import db, login_manager
from company import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))


class Login(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(30), unique=True, nullable=False)
    location = db.Column(db.String(50), nullable=False, unique=False)
    designation = db.Column(db.String(20), nullable=False, unique=False)
    details = db.relationship('Details', backref='e_id', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)


class Details(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    name = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email_id = db.Column(db.String(20), unique=True, nullable=False)

class Oxygen(db.Model):

    __bind_key__ = 'delhi'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    input = db.Column(db.Integer, nullable=False)
    output = db.Column(db.Integer, nullable=False)
    sensor_status = db.Column(db.String(10), unique=False, nullable=False)
    spread_medium = db.Column(db.String(15), unique=False, nullable=False)
    degree_of_damage = db.Column(db.String(8), unique=False, nullable=False)
    material_of_container = db.Column(db.String(20), unique=False, nullable=False)
    date = db.Column(db.DATE, nullable=False, unique=True)

class Hydrogen(db.Model):

    __bind_key__ = 'delhi'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    input = db.Column(db.Integer, nullable=False)
    output = db.Column(db.Integer, nullable=False)
    sensor_status = db.Column(db.String(10), unique=False, nullable=False)
    spread_medium = db.Column(db.String(15), unique=False, nullable=False)
    degree_of_damage = db.Column(db.String(8), unique=False, nullable=False)
    material_of_container = db.Column(db.String(20), unique=False, nullable=False)
    date = db.Column(db.DATE, nullable=False, unique=True)

class Chlorine(db.Model):

    __bind_key__ = 'delhi'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    input = db.Column(db.Integer, nullable=False)
    output = db.Column(db.Integer, nullable=False)
    sensor_status = db.Column(db.String(10), unique=False, nullable=False)
    spread_medium = db.Column(db.String(15), unique=False, nullable=False)
    degree_of_damage = db.Column(db.String(8), unique=False, nullable=False)
    material_of_container = db.Column(db.String(20), unique=False, nullable=False)
    date = db.Column(db.DATE,nullable=False,unique=True)

class Plant(db.Model):

    __bind_key__ = 'delhi'
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    vents = db.Column(db.Integer, nullable=False)
    number_of_sensors = db.Column(db.Integer, nullable=False)
    power_consumption = db.Column(db.Integer, nullable=False)
    water_sources = db.Column(db.String(10), unique=False, nullable=False)
    nearby_mountains = db.Column(db.String(10), unique=False, nullable=False)
    distance_from_domestic_area = db.Column(db.Integer, nullable=False)