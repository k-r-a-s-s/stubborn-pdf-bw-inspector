# stubborn-pdf-bw-inspector
Helps to determine how many pages of pdfs were black and white vs colour

use the bash command here (inspired by post from Kurt Pfeifle https://stackoverflow.com/a/25645224/18724266):

```
for i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt; donefor i in *.pdf; gs -q  -o - -sDEVICE=inkcov "$i" | grep -v '^ 0.00000  0.00000  0.00000' > "$i".txt
```

in the folder with pdf(s) to output text files containing the CMYK data in to a text file named after the name of the pdf. Requires ghostscript. 

Then use this python file to parse the text file(s). It compares and outputs a summary CSV totally the number black & white / colour pages


