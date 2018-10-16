from urllib.request import urlretrieve
import re

'''URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

print("Downloading File")
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z:print('.', end='', flush=True) if x % 100 == 0 else False)
'''

FILE_NAME = '/Users/antone/TCMG476_Project3/local_copy.log'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

line = fh.readline()
# Loop through the file
while line:
  #print(line)
  line = fh.readline()

fh.close()
things = []

# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open(FILE_NAME):

  # Use the Regex module to split out the filename from the line
  pieces = line.split(" ")
  things.append(pieces)

lineTotal = 0
for line in things:
    lineTotal += 1

print("Total requests " + str(lineTotal))

count400 = 0
for line in things:
    if len(line) > 9:
        if line[8][0] == '4':
            count400 += 1
print ("4xx requests " + str(count400))

count300 = 0
for line in things:
    if len(line) > 9:
        if line[8][0] == '3':
            count300 +=1
print("3xx requests " + str(count300))

countOct = 0
for line in things:
    if len(line) > 9:
        if line[3][4] == 'O':
            countOct +=1
print("October requests " + str(countOct))

countNov = 0
for line in things:
    if len(line) > 9:
        if line[3][4] == 'N':
            countNov +=1
print("November requests " + str(countNov))


oct = "oct"
nov = "nov"
countMD = [[oct,nov], [1,2,3]]
print(countMD[0],[0])



