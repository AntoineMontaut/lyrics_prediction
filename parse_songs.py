import os

artists = ['beatles', 'direstraits', 'eminem', 'madonna']

for artist in artists:
	path = 'other_artists/' + artist + '/'
	print(path)
	for filename in os.listdir(path):
		with open(path+filename, 'r', encoding='utf-8') as f:
			lyrics = f.read()
		
			# anchor before which song name is and after which song lyrics are
			user_agreement = "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"
			anchor = lyrics.find(user_agreement)

			# get the proper song name
			song_name = filename.rstrip('.html')

			# find where lyrics start in the html file
			beg = anchor
			end = lyrics[beg:].find('</div>')
			lyrics = lyrics[beg + len(user_agreement) : beg + end]
			#clean the lyrics
			lyrics = lyrics.replace('<i>','')
			lyrics = lyrics.replace('</i>','')
			lyrics = lyrics.replace('<br>', '\n')

			path_save = 'lyrics/' + artist + '/' + song_name + '.txt'
			if os.path.exists(path_save):
				print('{} has already been saved in a .txt file'.format(song_name))
			else:
				f = open(path_save, 'w', encoding='utf-8')
				f.write(lyrics)
				f.close()

				print('{} saved to a .txt file'.format(song_name))