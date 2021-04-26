"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from app.models import Favourites, Cars, Users
import psycopg2
#from app.forms import AddNewCarForm()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

###
# Routing for your application.
###  

@app.route('/') 
def home():
    """Render website's home page."""
    return app.send_static_file('index.html')

#Returns all cars from database and adds cars to DB
@app.route ('/api/cars', methods=['POST','GET'])
def returncars():
    carlist = []
    rootdir=os.getcwd()
    path=rootdir+ '/uploads'
    db = connect_db()
    cur = db.cursor()

    if request.method == 'GET':
        cur.execute('select * from "cars"')
        carinfo = cur.fetchall()
        db.commit()
        for info in carinfo
            cardetails=[{
                "description":info[1],
                "make":info[2],
                "model":info[3],
                "colour":info[4],
                "year":info[5],
                "transmission":info[6],
                "car_type":info[7],
                "price":info[8],
                "photo":info[9],
                "user_id":info[10]
            }]
        cur.close()
        for subdir, dirs, files in os.walk(path):
            for car in files:
                if car.endswith(('.png','.PNG', '.jpg','.JPG', '.jpeg','JPEG')):
                    carlist.append(car)
                    carimglist = [{"carimage":carlist}]

        return jasonify(cardetails=cardetails, carimglist=carimglist)

    if request.method == 'POST':
        if form.validate_on_submit:
            form = AddNewCarForm()
            #save image in uploads folder
            car_img=form.photo.data
            filename=secure_filename(car_img.filename)
            car_img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #Retrieve car info from form
            #Insert info into database
            cur.execute('insert into "cars" ("Description","Make","Model","Color","Year","Transmission","Car Type","Price,"Photo","User ID")values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(request.form['description'], request.form['make'],request.form['model'],request.form['colour'],request.form['year'],request.form['transmission'],request.form['cartype'],request.form['price'],filename,request.form['user_id']))
            db.commit()
            cur.close()
            #flash('New Vehicle added', 'success')
            jsonify(message="New Vehicle added Successfully") 
            #redirect(url_for('/api/cars'))

    #return render_template('index.html')

'''
#Adds new car to database
@app.route ('/api/cars', methods=['POST','GET'])
def addnewcar():
    form = AddNewCarForm()
    db = connect_db()
    cur = db.cursor()
    if request.method == 'POST': 
        if form.validate_on_submit:
            #save image in uploads folder
            car_img=form.photo.data
            filename=secure_filename(car_img.filename)
            car_img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #Retrieve car info from form
            #Insert info into database
            cur.execute('insert into "cars" ("Description","Make","Model","Color","Year","Transmission","Car Type","Price,"Photo","User ID")values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(request.form['description'], request.form['make'],request.form['model'],request.form['colour'],request.form['year'],request.form['transmission'],request.form['cartype'],request.form['price'],filename,request.form['user_id']))
            db.commit()

            flash('New Vehicle added', 'success')
            redirect(url_for('/api/cars'))
    return #return render_template(' ') new car form

'''



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
