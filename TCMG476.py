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

things = []
ERRORS = []

countTotal = 0
count400 = 0
count300 = 0

calendar = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open(LOCAL_FILE):
  countTotal += 1
  #if countTotal > 10:
    #break
  # Use the Regex module to split out the filename from the line
  # pieces = line.split(" ")
  pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)

  #print(pieces)

  if not pieces or len(pieces) < 8:
    ERRORS.append(line)
    continue

  statusCode = pieces[6]
  filename = pieces[4]
  requestDate = datetime.strptime(pieces[1], '%d/%b/%Y')

  if countTotal % 1000 == 0:
    print(".",end='')

  #check status code
  if statusCode[0] == '4':
    count400 += 1

  if statusCode[0] == '3':
    count300 += 1

  #break the log into months
  calendar[requestDate.month].append(line)

print("Total requests " + str(countTotal))

for k,v in calendar.items():
  #print("Month = {}, Values = {}".format(k,len(v)))
  filename = "{}.log".format(k)
  with open(filename, mode='w') as fh:
    fh.write("".join(v))
    fh.close()



# for line in open('/Users/antone/TCMG476_Project3/local_copy.log'):
#   # Use the Regex module to split out the filename from the line
#   pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)
#
#   date = pieces[1]
#   filename = pieces[4]
#   statusCode = pieces[6]
#
#   if filename in things:
#    # So we've already added this file -- let's increment the counter
#     things[filename] += 1
#   else:
#     # This is a new filename -- let's add it to the dictionary
#    things[filename] = 1


# sort by value to find highest
