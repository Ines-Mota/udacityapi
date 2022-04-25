from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#to connect app to a database we use sqlalchemy and the following code

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Armlockki9789@127.0.0.1:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__= 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    def __repr__(self):
     return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all() #creates the tables for models that don't exist yet

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello' + person.name

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
