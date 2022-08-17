import os
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
  
   return "Hello from A  Welcome to Test part 3333"
 
if __name__ == "__main__":
   app.run()
