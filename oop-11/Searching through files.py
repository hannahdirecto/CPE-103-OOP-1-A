fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('from:'):
      print(line)

fhand = open('mbox-short.txt')
for line  in fhand:
    line = line.rstrip()
    if line.startswith('from:'):
      print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #Skip 'uninterestingi lines'
    if not line.startswith('from:'):
      continue
    #Process our 'interesting' line
    print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)