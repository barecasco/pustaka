import os

# stylesheet insertion to add google fonts
insertCss = '<link rel="stylesheet"\
      href="https://fonts.googleapis.com/css2?family=Lora&family=Raleway&family=Roboto+Mono">'

# get current folder name
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
bookname = foldername

# build the book
os.system('cmd /c "npx honkit build"')

# copy the book with the folder name
os.system('cmd /c "xcopy /s /i _book {}"'.format(bookname))

# get the index file
flines = []
with open("{}/index.html".format(bookname), "r") as indexf:
  for line in indexf:
    stripped_line = line.strip()
    flines.append(stripped_line)
    if "generator" in stripped_line:
        flines.append(insertCss)

indexf = open("{}/index.html".format(bookname), "w")
for line in flines:
    indexf.write(line+"\n")
indexf.close()

# move the build folder to builds
os.system('cmd /c "echo a | xcopy /s /i {} ..\\..\\builds\\{}"'.format(bookname, bookname))

# erase _book
os.system('cmd /c "rmdir /s /q {}"'.format(bookname))
os.system('cmd /c "rmdir /s /q _book"')
