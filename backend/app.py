from models.user import User, user_schema, users_schema
from flask import Flask, request, jsonify
from database import db
from database import ma

import os

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# database
# to supress the warning on the terminal, specify this line
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test1234@localhost/dengue_stop'
# init extensions
db.init_app(app)
ma.init_app(app)
<<<<<<< HEAD


@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        telephone = request.json['telephone']
        first_name = request.json['firstName']
        last_name = request.json['lastName']
        nic_number = request.json['nicNumber']
        email = request.json['email']
        password = request.json['password']
        salt = request.json['salt']
        new_user = User(telephone, first_name, last_name,
                        nic_number, email, password, salt)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    except IOError:
        print("I/O error")
    except ValueError:
        print("Value Error")
    except:
        print("Unexpected error")
        raise
=======
>>>>>>> Move sqlalchemy and marshmallow initialization to database.py to avoid cyclic dependency



# running server
if __name__ == '__main__':
    app.run(debug=True)
