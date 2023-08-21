#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
import os 
from menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
app = Flask(__name__)

@app.route('/')
def display_menu():
    return render_template('menu.html')

@app.route('/filter/rating', methods=['GET', 'POST'])
def filter_by_rating_route():
    if request.method == 'POST':
     
       
        # Validate rating 
        try:
            rating = int(request.form['rating'])
            if 1 <= rating <= 10:
                print("Valid rating..")
                by_rating = Filter_by_rating()
                rows = by_rating.filter(rating)
            
            else:
                print("Rating must be between 1 and 10")
        except ValueError:
            print("Rating must be a valid integer..")

        print(rows)
        dict_data = []
        for title,price_per_night,prop_type in rows:
           dict_data.append({'title':title,'price_per_night':price_per_night,
                             'property_type':prop_type})
       
        print(dict_data)
        
        return jsonify(dict_data)
    return render_template('filter_rating.html')


@app.route('/filter/price', methods=['GET', 'POST'])
def filter_by_price_route():
    if request.method == 'POST':

        try:
           min_price = float(request.form['min_price'])
           max_price = float(request.form['max_price'])
           if max_price > min_price:
              print("Valid min price and max price..")

              by_price = Filter_by_price()
              rows = by_price.filter(min_price,max_price)
           else:
              print("Max price must be greater than min price..")
        except ValueError:
            print("Max price and min price must be floating numbers..")

        dict_data = []
        for title,price_per_night,prop_type in rows:
           dict_data.append({'title':title,'price_per_night':price_per_night,
                             'property_type':prop_type})    
        print(dict_data)
        
        return jsonify(dict_data) 
    return render_template('filter_price.html')




@app.route('/quit')
def quit():
    return "Goodbye!"
#app.run(debug=True)
app.run(host="0.0.0.0")
