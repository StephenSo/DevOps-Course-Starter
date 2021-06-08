from flask import Flask
from todo_app import app
#from todo_app.app import app as application

if __name__ == "__main__":
    app.run()
    #application.run()

flask_app = app.create_app()