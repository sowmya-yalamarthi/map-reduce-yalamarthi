n = open("out1.txt","r")  # open file, read-only
s = open("out2.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()