from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

print("Downloading File")
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z:print('.', end='', flush=True) if x % 100 == 0 else False)

FILE_NAME = '/Users/antone/PycharmProjects/TCMG476-Project3/local_copy.log'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

# Loop through the file
for line in fh:
  print(line)