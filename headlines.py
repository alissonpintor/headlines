from flask import Flask
from flask import render_template
from flask import request
import feedparser as feed

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'cdh': 'http://www.clubedohardware.com.br/pagesrssfeed.xml/'}


app = Flask(__name__)

@app.route('/')
def get_news():
    r = request.args.get('publication')
    client_ip = request.remote_addr
    if not r or r.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = r.lower()
    f = feed.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=f['entries'], client_ip=client_ip)

'''
@app.route('/')
@app.route('/bbc')
def bbc():
    return get_news('bbc')

@app.route('/cnn')
def cnn():
    return get_news('cnn')


@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    f = feed.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=f['entries'])
'''

if __name__ == '__main__':
    app.run(port=5000, debug=True)
