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
    facebook_url = websites_data['facebook_url']
    linkedin_url = websites_data['linkedin_url']
    instagram_url = websites_data['instagram_url']
    github_url = websites_data['github_url']
    return render_template('index.html', name=name, facebook_url=facebook_url, linkedin_url=linkedin_url,
                            instagram_url=instagram_url, github_url=github_url)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2101)
