from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://root:3yGWpZ7jeS@34.78.116.136:27017/')
db = client['amitdata']


@app.route('/')
def index():
    websites_data = db.websites.find_one({'name': 'Amit Dahan'})
    name = websites_data['name']
    youtube_url = websites_data['youtube_url']
    linkedin_url = websites_data['linkedin_url']
    ynet_url = websites_data['ynet_url']
    return render_template('index.html', name=name, youtube_url=youtube_url, linkedin_url=linkedin_url,
                            ynet_url=ynet_url)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2101)


