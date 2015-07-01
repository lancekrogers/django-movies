import csv

print("Converting users...")
with open("movie-data/users.dat", encoding="windows-1252") as infile:
 reader = csv.reader((line.replace("::", ";") for line in infile),
                     delimiter=";")
 with open("movie-data/users.csv", "w", newline="") as outfile:
     writer = csv.writer(outfile)
     for row in reader:
         writer.writerow(row)