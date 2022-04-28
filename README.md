# stubborn-pdf-bw-inspector
Helps to determine how many pages of pdfs were black and white vs colour.

If you have word documents, consider using https://github.com/AlJohri/docx2pdf to convert them.

use the bash command here (inspired by post from Kurt Pfeifle https://stackoverflow.com/a/25645224/18724266):

```
for i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt; donefor i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt
```

in the folder with pdf(s) to output text files containing the CMYK data in to a text file named after the name of the pdf. Requires ghostscript. 

Then use this python file to parse the text file(s). It compares the CMYK looking for C==M==Y and assumes that this is b&w. There may be some false psotives and false negatives with this method, but has been very consistent with my sample pdfs.
The output is a summary CSV tallying the number black & white / colour pages.



Example bulk conversion process for word docs:
```
from docx2pdf import convert

mypath = "/Users/MYname/FolderOfWordDocs"

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

print(dirnames)
```

