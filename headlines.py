from flask import Flask
import feedparser as feed

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


app = Flask(__name__)

'''
@app.route('/')
@app.route('/bbc')
def bbc():
    return get_news('bbc')

@app.route('/cnn')
def cnn():
    return get_news('cnn')
'''

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    f = feed.parse(RSS_FEEDS[publication])
    first_article = f['entries'][0]
    return '''
        <html>
            <body>
                <h1> ClubeDoHardware Headlines </h1>
                <b>{0}</b> <br/>
                <i>{1}</i> <br/>
                <p>{2}</p> <br/>
                <p>Qtd: {3}</p>
            </body>
        </html>
    '''.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"), len(first_article))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
