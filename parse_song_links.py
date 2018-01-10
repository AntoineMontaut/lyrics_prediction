with open('megadeth_songs.html', 'r', encoding='utf-8') as songs_file:
	songs_all = songs_file.read().replace('\n', '')

target = "songlist = ["
beg = songs_all.find("songlist = [")
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



# print(links)