
from flask import Flask, request
from flask_restful import Api,Resource,reqparse
import db

app1 = Flask(__name__)
api = Api(app1)

class Students(Resource):

    def get(self):

        return db.get_students()


class Names(Resource):

    def get(self):
        email = request.args["email"]
        # parser.add_argument('email', type= str)
        print(email)
        
        # args = parser.parser_args()
        # email = args['email']

        return db.get_name(email)

api.add_resource(Students, "/students")
api.add_resource(Names, "/name")

if __name__ == "__main__":
    app1.run('0.0.0.0')







# FROM python:3

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip3 install -r requirements.txt

# COPY . /app

# ENTRYPOINT [ "python3" ]

# CMD [ "test.py" ]
