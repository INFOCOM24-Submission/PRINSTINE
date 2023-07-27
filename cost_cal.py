import sys
fp = sys.argv[1]
ts = [0]*4

ind = 0
with open(fp) as f:
	line = f.readline()
	while line:
		if "time" in line:
			ind +=1
			line = f.readline()
			continue
		
		line = line.split()
		sent = eval(line[4])
		rec = eval(line[7])
		ttl = sent + rec
		ts[ind] += ttl
		line = f.readline()
ts[2] = ts[0] + ts[1]
print(ts)
	
