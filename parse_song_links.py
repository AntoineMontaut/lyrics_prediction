import requests
import re
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with open('megadeth_songs.html', 'r', encoding='utf-8') as songs_file:
	songs_all = songs_file.read().replace('\n', '')

target = "songlist = ["
beg = songs_all.find(target)
end = songs_all[beg:].find("];")

songs_list = songs_all[beg + len(target) : beg + end]

songs = songs_list.split('},{')
songs[0] = songs[0][1:]
songs[-1] = songs[-1][:-1]

links = []
for song in songs:
	link = song.split(', ')[1]
	link = link.lstrip('h:"../').rstrip('"')
	links.append(link)


url_base = 'https://www.azlyrics.com/lyrics/'
url_artist = 'megadeth/'

# link = links[0]

for link in links[:5]:
	file_name = link.split('/')[-1]
	# song_name = file_name.replace('.html', '')
	full_url = url_base + url_artist + file_name

	# get the lyrics for a specific song
	page = requests.get(full_url, headers=headers)
	lyrics = page.text.replace('\n', '')
	# print(lyrics)

	# anchor before which song name is and after which song lyrics are
	user_agreement = "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"
	anchor = lyrics.find(user_agreement)

	# get the proper song name as displayed on the website
	target='&quot;'
	beg = lyrics.find(target)
	end = lyrics[beg + 1:].find(target)
	# print(start, end)
	print(lyrics[beg + len(target) : beg + end + 1])

	# find where lyrics start in the html file
	beg = anchor
	end = lyrics[beg:].find('</div>')
	lyrics = lyrics[beg + len(user_agreement) : beg + end]
	#clean the lyrics
	lyrics = lyrics.replace('<i>','')
	lyrics = lyrics.replace('</i>','')
	lyrics = lyrics.replace('<br>', '\n')

	# write the lyrics in a text file
	# f = open('lyrics/' + song_name + '.txt', 'w', encoding='utf-8')
	# f.write(lyrics)
	# f.close()

	# print('{} imported'.format(song_name))
	# time.sleep(90)