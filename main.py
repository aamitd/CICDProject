from flask import Flask, render_template

app = Flask(__name__)


def get_urls(name):
    youtube_url = f"https://www.youtube.com/user/{name.replace(' ', '')}"
    linkedin_url = f"https://www.linkedin.com/in/{name.replace(' ', '').lower()}"
    ynet_url = f"https://www.ynet.co.il/articles/byauthor/{name.replace(' ', '_')}"

    return youtube_url, linkedin_url, ynet_url


@app.route('/')
def index():
    name = "Amit Dahan"
    youtube_url, linkedin_url, ynet_url = get_urls(name)
    return render_template('index.html', name=name, youtube_url=youtube_url, linkedin_url=linkedin_url,
                           ynet_url=ynet_url)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5050)
