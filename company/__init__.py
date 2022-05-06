from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, template_folder=r'C:\Users\dexco\Desktop\intern_proj\company\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/company'
app.config['SQLALCHEMY_BINDS'] = {'delhi' : 'mysql+pymysql://root:@localhost/delhi'}
                                  #,'bangalore' : 'mysql+pymysql://root:@localhost/company'}

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = '4ac5d47ba1516b2880db1c69'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from company import routes
