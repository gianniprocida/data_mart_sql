from flask import Flask, render_template, request
from another_menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
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
        print("Hello!!!!")
        print(rows)
        # Perform filtering logic based on rating
        # Return the filtered results
        return render_template('filter_results.html',rows = rows)
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




@app.route('/quit')
def quit():
    return "Goodbye!"

if __name__ == '__main__':
    app.run(debug=True)