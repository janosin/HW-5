
import re


fh = open("regex_sum_31471.txt")
l = list()
for line in fh:
	y = re.findall("[0-9]+", line)
	for item in y:
		x = int (item)
		l.append(x)
s = 0
for i in l:
	s = i + s
print (s)
	
	