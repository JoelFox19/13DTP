#This code was created by Joel Fox in 2021
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)



#This query takes all of the images and names from the brands table and displays it on the home page(home.html)
@app.route('/')
def home():
   return render_template('home.html',title="Home Page")


if __name__=="__main__":
   app.run(debug=True)
   