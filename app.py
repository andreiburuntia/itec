# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

# create the application object
app = Flask(__name__)

# set key as config
app.config['GOOGLEMAPS_KEY'] = 'AIzaSyDTVi9ReyAXCk1MoBpJHrGUi8o8IkeVl0M'

# gmaps init
GoogleMaps(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "route me"  # return a string

@app.route('/map')
def map():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=45.7489,
        lng=21.2087,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 45.7489,
             'lng': 21.2087,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 45.7489,
             'lng': 21.2087,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)