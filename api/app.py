#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
from kafka import KafkaProducer,KafkaConsumer
from menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
from myproducer import connect_kafka_producer,publish_message
from confluent_kafka import Producer
import json
import time
import datetime
from database_utils import getConn
from connection_utils import check_connection
import os,base64
import logging
from time import gmtime
from string_producer import *
from string_producer import _full_path_of
from certificate_utils import decode_certificate
import base64





app = Flask(__name__)



@app.route('/')
def display_menu():
    return render_template('menu.html')

@app.route('/filter/rating', methods=['GET', 'POST'])
def filter_by_rating_route():
    if request.method == 'POST':
        rating = request.form['rating']
        print("I am here")
        print(rating)
        by_rating = Filter_by_rating()
        rows= by_rating.filter(rating)
        dict_data = []
        for a,b,c,d,f in rows:
           dict_data.append({'a':a,'b':b,'c':c,'d':d,'f':f})
       
        print(dict_data)
          # Perform filtering logic based on rating
          # Return the filtered results
        return jsonify(dict_data)
    return render_template('filter_rating.html')

@app.route('/filter/price', methods=['GET', 'POST'])
def filter_by_price_route():
    if request.method == 'POST':
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        by_price = Filter_by_price()
        rows = by_price.filter(min_price,max_price)
        print(rows)
        # Perform filtering logic based on price range
        # Return the filtered results
        return render_template('filter_results.html',rows=rows)
    return render_template('filter_price.html')



@app.route('/update/users',methods=['GET','POST'])
def update_users():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone_number']
        dob_str = request.form['DoB']
        gender = request.form['gender']
        country = request.form['country']
        user_type = request.form['user_type']
        

        #Validate DoB as a date format
        try:
            dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d')
        except ValueError:
            return 'Invalid date format for DoB',400
        
        #Validate gender
        if gender not in ["Male","Female"]:
            return 'Invalid gender value',400
        
        # Validate user_typr
        if user_type not in ["guest","host"]:
            return 'Invalid user_type'


        row = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number':phone,
        'email': email,
        'DoB':dob_str,
        'gender':gender,
        'country':country,
        'user_type':user_type
       }
        

        logger = logging.getLogger('')  # Root logger, to catch all submodule logs
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d|%(levelname)s|%(filename)s| %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
        formatter.converter = gmtime  # Log UTC time

        
        axual_host = os.environ.get("bootstrap.servers")
        axual_port = os.environ.get("port")

        bootstrap_servers = f"{axual_host}:{axual_port}"

       
      
        print(" ")

        print("I am about to print...")

        
        decode_certificate("/app/client-cert/client.pem","/tmp/client.pem")

        decode_certificate("/app/client-cert/clientkey.pem","/tmp/clientkey.pem")
      


        
       
        topic = os.environ.get("topic")
        configuration = {
         'bootstrap.servers': bootstrap_servers,
         # SSL configuration
         'security.protocol': "SSL",
         'ssl.endpoint.identification.algorithm': "none",
         'ssl.certificate.location': _full_path_of("/tmp/client.pem"),
         'ssl.key.location':_full_path_of("/tmp/clientkey.pem"),
         'ssl.ca.location':_full_path_of("/tmp/client.pem"),
         'acks': "all",
#         'debug': debug,
         'logger': logger
     }
                

        print("Our data..",row)

        print("bootstrap_servers...",bootstrap_servers)

        print("my topic ...",topic)


        produce_data(configuration,topic,row,logger)
        
  
    return render_template('update_Users.html') 

@app.route('/update/reservations',methods=['GET','POST'])
def update_reservations():
    if request.method == 'POST':
        print("welcome")

    return render_template('update_Users.html') 


@app.route('/quit')
def quit():
    return "Goodbye!"

app.run(host="0.0.0.0")
