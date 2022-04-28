# scans pdf
# use the bash script here (inspired by post from Kurt Pfeifle https://stackoverflow.com/a/25645224/18724266)
# for i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt; donefor i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt
# in the folder with pdfs to output text files containing the CMYK data in to a text file named after the name of the pdf
# requires ghostscript, 
# then this python file parses those text files, compares and spits out when it is black and white or colour on a page



import os
import pandas as pd
import csv


path = 'FILEPATH_TO/PDFS/here/'



filenames = []
filepaths = []
blackwhite = []
colour = []

with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".txt") and entry.is_file():
            filenames.append(entry.name)
            filepaths.append(entry.path)
            df = pd.read_fwf(entry.path,names=["C", "M", "Y", "K","foo","bar"])
            df['black'] = (df.C == df.M) & (df.C == df.Y)
            blackwhite.append(df['black'].sum())
            colour.append((~df['black']).sum())

rows = zip(filenames, filepaths, blackwhite, colour)
headers = ('filenames', 'filepaths', 'blackwhite', 'colour')



with open('outputcsv.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)





