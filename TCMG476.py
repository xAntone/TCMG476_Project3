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
ERRORS = []

# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open(FILE_NAME):

  # Use the Regex module to split out the filename from the line
  pieces = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
  #print(pieces)
  things.append(pieces)

  regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

  # Call the split() method to get all the capture groups put in a list
  parts = regex.split(line)

  # Let's see what the regex grabbed...
  print(parts)

  # Sanity check the line -- there should be 7 elements in the list (remember that index 0 has the whole string)
  if not parts or len(parts) < 7:
    print("Error parsing line! Log entry added to ERRORS[] list...")
    ERRORS.append(line)
  else:
    print("\n")

number = 0
size = len(things)
counter = 0
while(counter < size):
  if things[counter][6][0] == "4":
    number += 1
  counter += 1

print(number)




for line in things:
    if line[6][0] == "4":
      number += 1
print("400 % = " + str(number))


  # Let's further say that we can get the filename part at the 4th list element
print("Length of array")
print (len(things))
print("\n")

print("First line")
print(things[0])
print(things[0][6][0])
print("\n")

print("Last Line")
print(things[43538])




'''
# print("\nErrors: " + str(len(ERRORS)))
#print(ERRORS)

count3 = 0
count4 = 0
for i in range(0,len(things)):
  print(i)
  if str(things[i][6]).startswith("4"):
    count4 += 1
  elif str(things[i][6]).startswith("3"):
    count3 += 1

print(count4)
print(count3)
'''