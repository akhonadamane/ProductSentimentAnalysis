
PROGRAM STRUCTURE

flask_sentiment_analysis/
│
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html          # Base HTML template for top bar
│   ├── index.html         # Main page where users enter their sentiments
│   ├── users_input.html   # User input page for entering sentiment
│   └── dashboard.html     # Sentiment analysis dashboard
├── static/
│   ├── styles.css         # CSS for styling the web pages
└── sentiment_model.py     # Logic for Hugging Face sentiment analysis





DETAILS / REQUIREMENTS: 

Webinterface (with top bar with "Users input" button and "Sentimental Analysis Dashboard"). On the body of the main page write "Share how you feel or think about each of these South African favourite non-alcoholic beverages". The users input page will allow 10 users input of their sentiments about 5 predefined non-alcoholic drinks (brand / products): Coke, Amasi, Stoney Ginger, AmaHewu, Rooibos Tea (in natural everyday language) (with page refreshing for each user, first user page followed by the second, until the 10th user). For the sentimental analysis dashboard page, each product should have a rating whether positive or negative.