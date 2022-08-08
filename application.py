
from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "HELLO, AWS"

@application.route("/help")
def help():
    return "<b><font color=blue>Help page</font></b>"

@application.route("/user")
def user():
   return "<h>USERS</h>"

@application.route("/user/<username>")
def shown_username(username):
   return "Hello " + username.upper()

@application.route("/path/<path:subpath>")
def print_subpath(subpath):
   return "Subpath is: " + subpath

@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
   return "Kvadrat ot: " + str(x) + " = " + str(x*x)

@application.route("/main")
def main_page():
   myfile = open("main.html", mode='r')
   page   = myfile.read()
   myfile.close()
   return page 

if __name__ == "__main__":
   #application.debug = True
   #application.env = "Testing"
   application.run()
