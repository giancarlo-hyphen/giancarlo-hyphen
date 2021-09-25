# Make a while loop of all of this to make it more neat
# import statements
import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
stdoutOrigin=sys.stdout
sys.stdout = open("linuxjobb.txt", "w")
#jobb = 'fritidslärare'
# Get links
# URL of a WebPage
#def pagenumberprint(tag):
pagenumber = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]

url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[0]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[1]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[2]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[3]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[4]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[5]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[6]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[7]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[8]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[9]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[10]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[11]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[12]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[13]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  continue
url = "https://jobbsafari.se/lediga-jobb?q=Linux&filters=stockholms-lan&sort=PUBLISHED&page=" + pagenumber[14]

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')


#Prints all the links in the list tags
for tag in tags:
  # Get the data from href key
  print(str("www.jobbsafari.se") + tag.get('href', None), end = "\n")
  break
sys.stdout.close()




