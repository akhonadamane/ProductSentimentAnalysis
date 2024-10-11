from flask import Flask, render_template, request, redirect, url_for, session
from sentiment_model import analyze_sentiment

app = Flask(__name__)
app.secret_key = "some_secret_key"  # For session handling

# A list to store user inputs
user_sentiments = []
max_users = 10

# Product list
products = ['Coke', 'Amasi', 'Stoney Ginger', 'AmaHewu', 'Rooibos Tea']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users_input', methods=['GET', 'POST'])
def users_input():
    if len(user_sentiments) >= max_users:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        user_input = {}
        for product in products:
            user_input[product] = request.form[product]
        user_sentiments.append(user_input)

        # If we have max number of users, redirect to the dashboard
        if len(user_sentiments) >= max_users:
            return redirect(url_for('dashboard'))

        return redirect(url_for('users_input'))
    
    return render_template('users_input.html', user_num=len(user_sentiments)+1, products=products)

@app.route('/dashboard')
def dashboard():
    sentiment_results = {}
    for product in products:
        sentiments = [user[product] for user in user_sentiments]
        result = analyze_sentiment(sentiments)
        sentiment_results[product] = result

    return render_template('dashboard.html', sentiments=sentiment_results, products=products)

if __name__ == "__main__":
    app.run(debug=True)
