# Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
# Solution 
+ Use the imagemagick library to convert the pdf to jpg.
```bash
$ sudo apt-get install imagemagick
```
+ Then you can use the convert funtion like this.
```bash
convert <FIleName.pdf> <OutputName.jpg>
```
