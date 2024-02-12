import re

text = "Best Friend In The World (2017), 01-10-2000, ISBN 123-4-123-12345-1, 192.098.190.075, #ffffff, Fish S01E02:Little Friend, @choldaniel, [Verse 1] I love you..., Why did the car run ? Because nothing"

# Regular Expression Patterns
movie_title_regex = r'.*?\s\(\d{4}\)'#Matches movie titles with the year in parentheses.
date_regex = r'\d{2}-\d{2}-\d{4}'#Matches dates in the format DD-MMM-YYYY.
isbn_regex = r'ISBN \d{3}-\d-\d{3}-\d{5}-\d'# Matches ISBN numbers.
ip_address_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'##Matches IP addresses.
hex_color_regex = r'#([A-Fa-f0-9]{6})'#Matches hex color codes.
tv_episode_regex = r'\bFish S\d{1,2}E\d{1,2}:[^,]+'#Matches TV episode titles.
song_lyrics_regex = r'\[(\w+ \d+)\]\s(.*?)\.\.\.'#Matches song lyrics enclosed in square brackets, capturing both the section and the lyrics.
twitter_username_regex = r'@\w+'##Matches Twitter usernames.
jokes_regex = r'Why did the .*? Because[^,]+'##Matches jokes.

# Extracting Data using Regular Expressions
##re.findall() is use to extract inform. from the given text based on the defined regular expressions above 
movie_titles = re.findall(movie_title_regex, text)
dates = re.findall(date_regex, text)
isbn_numbers = re.findall(isbn_regex, text)
ip_addresses = re.findall(ip_address_regex, text)
hex_colors = re.findall(hex_color_regex, text)
tv_episode_titles = re.findall(tv_episode_regex, text)
song_lyrics = re.findall(song_lyrics_regex, text)
twitter_usernames = re.findall(twitter_username_regex, text)
jokes = re.findall(jokes_regex, text)

# This section specifically targets song lyrics using the song_lyrics_regex.
# It extracts matches and creates an array of tuples (lyrics_array),
# where each tuple contains the section and lyrics, adding ellipses at the end.
matches = re.findall(song_lyrics_regex, text)
lyrics_array = [(section, lyrics + '...,') for section, lyrics in matches]

# Printing Extracted Data
#These lines print the extracted data for each category,
# providing a structured output for better readability.
print("Movie Titles:", movie_titles)
print("Dates:", dates)
print("ISBN Numbers:", isbn_numbers)
print("IP Addresses:", ip_addresses)
print("Hex Color Codes:", hex_colors)
print("TV Episode Titles:", tv_episode_titles)
print("Song Lyrics:", lyrics_array)
print("Twitter Usernames:", twitter_usernames)
print("Jokes:", jokes)

