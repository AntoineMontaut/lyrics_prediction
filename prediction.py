import os

path = 'lyrics/'
lyrics = []
for filename in os.listdir(path):
	with open(path+filename, 'r', encoding='utf-8') as f:
		lyrics.append(f.read().replace('\n', ''))

for lyric in lyrics:
	print(lyric)