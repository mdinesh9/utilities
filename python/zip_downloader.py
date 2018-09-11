# TODO
# Use cmd args to fetch the url 
# Detect the zip file name and use it to save


import urllib

url = "http://nlp.stanford.edu/data/glove.6B.zip"

print("Downloading urllib")
urllib.request.urlretrieve(url, "glove.6B.zip")