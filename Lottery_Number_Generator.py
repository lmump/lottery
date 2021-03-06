import urllib2

address = 'http://www.powerball.com/powerball/winnums-text.txt'
winstrings = urllib2.urlopen(address).readlines()
redtop = 69
whitetop = 26
lastdate = '08/31/2005'
redcounts = [0] * redtop
whitecounts = [0] * whitetop
headerline = winstrings.pop(0) # garbage

for winstring in winstrings:
    winelements = winstring.split(' ')
    date = winelements.pop(0) # garbage

for reds in range(5):
    redcounts[int(winelements.pop(0)) - 1] += 1
    whitecounts[int(winelements.pop(0)) - 1] += 1

if date == lastdate: break
pairedreds = zip(range(1, redtop + 1), redcounts)
pairedwhites = zip(range(1, whitetop + 1), whitecounts)
print "Red Ball counts"
for reds in pairedreds:
    print "%2d:%3d " % reds,
    if not (reds[0] % 4): print

print "\n\n\nPowerBall counts"
for whites in pairedwhites:
    print "%2d:%3d " % whites,
    if not (whites[0] % 4 ): print

# Now to choose the most commonly drawn numbers
# At least as many as need to be drawn
def chooseMaxes(pairedlist, numtochoose):
if numtochoose >= len(pairedlist): return pairedlist # can't choose more numbers than choices
maxlist = []
modalfreq = max(x[1] for x in pairedlist)

while True:
    maxlist.extend(x[0] for x in pairedlist if x[1] == modalfreq)
    if len(maxlist) >= numtochoose: return maxlist
    modalfreq -= 1

print "\n\n\nMost common red balls chosen were:",
print str(chooseMaxes(pairedreds, 5))[1:-1]
print "Most common power balls chosen were:",
print str(chooseMaxes(pairedwhites, 1))[1:-1]
