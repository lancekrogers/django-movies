import csv


print("Converting movies...")
with open("movie-data/movies.dat", encoding="windows-1252") as infile:
 reader = csv.reader((line.replace("::", ";") for line in infile),
                     delimiter=";")
 with open("movie-data/movies.csv", "w", newline='') as outfile:
     writer = csv.writer(outfile)
     for row in reader:
         writer.writerow(row)

print("Converting ratings...")
with open("movie-data/ratings.dat") as infile:
 reader = csv.reader((line.replace("::", ";") for line in infile),
                     delimiter=";")
 with open("movie-data/ratings.csv", "w", newline='') as outfile:
     writer = csv.writer(outfile)
     for row in reader:
         writer.writerow(row)


