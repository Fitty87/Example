from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager



# Create flask app
app = Flask(__name__, template_folder='templates')

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///common_database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Bootstrap
Bootstrap(app)

#Secret Key
app.config['SECRET_KEY'] = "my secret key" 

#Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True, render_as_batch=True) #render_as_batch=True

#LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





