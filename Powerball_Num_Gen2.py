import random
print "Ofical Powerball number generator"
x = int(raw_input("How many sets of numbers? "))
z = range(1,26)

for n in range(x):
  print 'Your numbers: ' + str(sorted(random.sample(range(1,69), 5))) + ' Powerball: ' + str(random.choice(z))
