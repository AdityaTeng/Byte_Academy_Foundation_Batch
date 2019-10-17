from requests_html import HTML, HTMLSession, AsyncHTMLSession

session = HTMLSession()
r = session.get('https://www.reddit.com/r/gameofthrones/')
r.html.render()

article = r.html.find('#t3_d9qwia')
print(article[0])