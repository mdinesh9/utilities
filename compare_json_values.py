# Compares two json files and prints the differences in the values.
# The keys were in ascending order in the two json files used here.


import json

with open("with_strip.json") as json_file:
    with_strip_data = json.load(json_file)

with open("without_strip.json") as json_file:
    without_strip_data = json.load(json_file)

for count in range(2,36779):
    if with_strip_data[str(count)] != without_strip_data[str(count)]:
        print count,':',with_strip_data[str(count)].encode('utf-8'),',',without_strip_data[str(count)].encode('utf-8')

