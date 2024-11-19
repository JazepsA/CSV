import csv
import json

songs=[]
year=[]
count_year=[]

with open("./spotify.csv","r",encoding="utf-8") as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        songs.append(line)
    
print(songs)

with open("./spotify.json","w",encoding="utf-8") as json_file:

    json.dump(songs,json_file,indent=4)

count=0

for song in songs:
    print(song['Title'])
    if song['Year'] not in year:
        year.append(song["Year"])

print(year)

song_count=0

for y in year:
    for song in songs:
        if song['Year']==y:
            song_count+=1
    
count_year.append(song_count)
print(year)
print(count_year)