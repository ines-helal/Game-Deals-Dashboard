from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():

    query = request.args.get('search')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    url = "https://www.cheapshark.com/api/1.0/deals"
    response = requests.get(url)
    games = response.json()

    if query:
        games = [game for game in games if query.lower() in game['title'].lower()]

    if min_price:
        games = [
            game for game in games
            if float(game['salePrice']) >= float(min_price)
        ]

    if max_price:
        games = [
            game for game in games
            if float(game['salePrice']) <= float(max_price)
        ]

    return render_template(
        'index.html',
        games=games,
        query=query,
        min_price=min_price,
        max_price=max_price
    )

if __name__ == '__main__':
    app.run(debug=True)