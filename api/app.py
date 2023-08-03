#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
from menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
import base64
import json
import time
import datetime
from database_utils import getConn
from connection_utils import check_connection
import logging
from os.path import dirname, abspath
from time import gmtime

from confluent_kafka import Producer


import os

app = Flask(__name__)

logger = logging.getLogger('')  # Root logger, to catch all submodule logs
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d|%(levelname)s|%(filename)s| %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
formatter.converter = gmtime  # Log UTC time

if len(logger.handlers) == 0:
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)


def _full_path_of(path):
    base_dir = dirname(dirname(dirname(abspath(__file__))))
    return f'{base_dir}{path}'


def delivery_callback(error, msg) -> None:
    """
    Per-message delivery callback (triggered by poll() or flush())

    :param error: None if the message was successfully delivered
    :param msg: Message metadata
    :return: None
    """
    if error is not None:
        logger.error(f'Failed to deliver message: {error}')
    else:
        logger.info(f'Produced record to topic {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}')


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_str = json.dumps(value)  # Serialize dictionary to JSON string
        value_bytes = bytes(value_str, encoding='utf-8')
        producer_instance.poll(0)
        producer_instance.produce(topic_name, key=key_bytes, value=value_bytes,on_delivery=delivery_callback)
      
    except Exception as ex:
        logger.error('Exception in publishing message')
        logger.error("%s",str(ex))
    finally:
        if producer_instance is not None:
            logger.info('Flushing producer.')
            producer_instance.flush()


kafka_host = os.environ.get("KAFKA_BROKER_HOST")
kafka_port = os.environ.get("KAFKA_BROKER_PORT")
topic = os.environ.get("TOPIC")
certLocation = str(os.environ.get("CERTLOCATION"))
clientPub = str(os.environ.get("CLIENTPUB"))
clientKey = str(os.environ.get("CLIENTKEY"))
ca = str(os.environ.get("CA"))

logging.info("Connection to %s:%s topic: %s",kafka_host,kafka_port,topic)
logging.info("%s %s %s %s",certLocation,clientPub,clientKey,ca)

# Kafka producer configuration
configuration = {
'bootstrap.servers': kafka_host + ":" + kafka_port,
# SSL configuration
'security.protocol': 'SSL',
'ssl.endpoint.identification.algorithm': 'none',
'ssl.certificate.location': _full_path_of(certLocation + '/' + clientPub),
'ssl.key.location': _full_path_of(certLocation + '/' + clientKey),
'ssl.ca.location': _full_path_of(certLocation + '/' + ca),
'acks': 'all',
# 'debug': 'all',
'logger': logger
}

producer = Producer(configuration)


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

        try:
            logger.info(f'Starting kafka producer to produce to topic: {topic}. ^C to exit.')
            record_key = f'key'
            publish_message(producer,topic, record_key,row)

            logger.info('Done producing.')
        except KeyboardInterrupt:
            logger.info('Caught KeyboardInterrupt, stopping.')     

    return render_template('update_Users.html') 

@app.route('/update/reservations',methods=['GET','POST'])
def update_reservations():
    if request.method == 'POST':
        print("welcome")

    return render_template('update_Users.html') 


@app.route('/quit')
def quit():
    return "Goodbye!"
#app.run(debug=True)
app.run(host="0.0.0.0")
