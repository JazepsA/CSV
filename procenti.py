import csv
import json

info=[]
varduVardnica=[]

with open("./jauns.csv","r",encoding="utf-8") as file:
    csvFile=csv.reader(file)
    for line in csvFile:
        print(line)

with open("./jauns.csv","r",encoding="utf-8") as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        info.append(line)



with open("./jauns.json","w",encoding="utf-8") as json_file:
    json.dump(info,json_file,indent=4)

for vards in info:
    if vards['Vards'] not in varduVardnica:
        varduVardnica.append(vards["Vards"])

print(varduVardnica)


for i in info:
    print(i['Vards'],i['Maksa par pusdienam'],"naudiņa")


kopa=0

for i in info:
    viens=int(i["Maksa par pusdienam"])
    kopa+=viens

print(f"{kopa} ir visu pusdienu kopsumma")

