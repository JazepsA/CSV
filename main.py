import csv

titles=[]
year=[]
with open("./spotify.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    for i in reader:
        titles.append(i[0])
        year.append(i[3])
    print(titles)
    print(titles[1::])
    print(list(set(year[1::])))