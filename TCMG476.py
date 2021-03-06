from urllib.request import urlretrieve
import re
import os.path
from datetime import datetime

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

#check to see if we have copy of file

if not os.path.isfile(LOCAL_FILE):
  # local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
  print("Downloading File")
  local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE,
                                    lambda x, y, z: print('.', end='', flush=True) if x % 100 == 0 else False)

# declare dictionaries
things = {}
ERRORS = []

# set counters to zero
countTotal = 0
count400 = 0
count300 = 0
countRequest = 0

#array within a dictionary
calendar = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open(LOCAL_FILE):
  countTotal += 1
  #if countTotal > 10:
    #break
  # Use the Regex module to split out the filename from the line
  pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)

  #show progress of requests being looped through
  print(pieces)

  #check for any requests that were bad
  if not pieces or len(pieces) < 8:
    ERRORS.append(line)
    continue

  #seperate the lines by each property
  statusCode = pieces[6]
  filename = pieces[4]
  requestDate = datetime.strptime(pieces[1], '%d/%b/%Y') #datetime module

  # progress bar
  if countTotal % 1000 == 0:
    print(".",end='')

  #check status code 4
  if statusCode[0] == '4':
    count400 += 1

  #check status code 3
  if statusCode[0] == '3':
    count300 += 1

  # break the log into months
  calendar[requestDate.month].append(line)

  if filename in things:
    # So we've already added this file -- let's increment the counter
    things[filename] += 1

  else:
    # This is a new filename -- let's add it to the dictionary
    things[filename] = 1

# get largest and smallest value from dic
max = (max(things, key=things.get))
min = (min(things, key=things.get))

# write requests to separate files based on months
for k,v in calendar.items():
  filename = "{}.log".format(k)
  with open(filename, mode='w') as fh:
    fh.write("".join(v))
    fh.close()

# work for Q2
four = (count400/countTotal)*100
three = count300/countTotal*100
day = (countTotal/365)
week = (countTotal/52)
month = (countTotal/12)

print("\n")
print("1. Total requests = " + str(countTotal))
print("   Average Requests Per: ")
print("2. Per Day: {} Per Week {} Per Month {}".format(day, week, month))
print("3. Percentage of requests not successful  = {0:.2f}%".format(four))
print("4. Percentage of requests redirected elsewhere = {0:.2f}%".format(three))
print("5. Most requested file = {}".format(max))
print("6. Least requested file = {}".format(min))