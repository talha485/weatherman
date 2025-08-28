import os, csv
folder="weatherfiles"
weather_data=[]
for files in os.listdir(folder):
    if files.endswith(".txt"):
        with open(os.path.join(folder,files),"r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                weather_data.append(row)
year=int(input("Enter year : "))
filter_data=[]
for row in weather_data:
    date = row.get("PKT","")
    if not date:
        continue
    parts = date.split("-")
    data_year=int(parts[0])
    if data_year == year:
        filter_data.append(row)

