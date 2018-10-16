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

  #print(line)
fh.close()

things = []

# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open(FILE_NAME):

  # Use the Regex module to split out the filename from the line
  pieces = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
  things.append(pieces)

  # Let's further say that we can get the filename part at the 4th list element
print(things[0][2])
print(things[0])
