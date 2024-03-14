from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/scrape/<path:url>', methods=['GET'])
def scrape(url):
    response = requests.get(f'https://{url}')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('src') for link in soup.find_all('img')]
    print(links)
    return jsonify(links)


if __name__ == "__main__":
    app.run(debug=True)

