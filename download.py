import requests

# header for the request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# get the desired page using get
page = requests.get(
    'https://www.azlyrics.com/m/megadeth.html', headers=headers)

# print(page.content)

f = open('megadeth_songs.html', 'w', encoding='utf-8')
f.write(page.text)
f.close()
