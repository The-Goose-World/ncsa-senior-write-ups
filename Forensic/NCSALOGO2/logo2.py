ncsa1 = open('./ncsa.png', 'rb').read()
ncsa2 = open('./ncsa2.png', 'rb').read()
fout = open('./flag.png', 'wb')
diff = ncsa2[len(ncsa1):]
fout.write(diff)