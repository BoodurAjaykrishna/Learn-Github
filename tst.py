


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
count = 0
emlist = []
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    
    em = line.split()
    if len(em) > 1:
        emlist.append(em[5])
        
           
#print(emlist)
hours = [int(t.split(':')[0]) for t in emlist]
print("list", hours)

for emls in hours:
    counts[emls] = counts.get(emls,0)+1

print("countssss", counts)
t = sorted(counts.items())
print("t", t)
for k,v in sorted(counts.items()):
    print(k,v)
bigcount = None
emails = None
for email, noof in counts.items():
    if bigcount is None or noof > bigcount:
        emails = email
        bigcount = noof
    
#print(emails,bigcount)

