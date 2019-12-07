crawler = 0
walker = 1
runner = None

for step in range(0,10):
	runner = crawler + walker
	crawler = walker
	walker = runner
	print(crawler)
	if walker % 2 == 0:
	  print(walker)

