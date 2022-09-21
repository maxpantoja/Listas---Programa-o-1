import imdb
import csv
ia = imdb.IMDb()
codes = [20880628, 10872600, 3501632, 9419884, 7131622]
colunas = ['imdbID', 'title', 'year', 'genres', 'kind']
linhas = []
for i in codes:
    linha = []
    series = ia.get_movie(i)
    for j in colunas:
        linha.append(series.data[j])
    linhas.append(linha)
with open('Filmes.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(colunas)
    write.writerows(linhas)
