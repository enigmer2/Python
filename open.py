f = open("file.txt", "r")
while f:
  l = f.readline()
  if not l:
    break
  if len(l) > 5:
    print l
f.close()
