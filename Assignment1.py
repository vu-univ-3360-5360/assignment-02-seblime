# import the json module
import json

# open the file. Complete the filename
f=open('tester.json')

# load JSON
datastore = json.load(f)

#complete the next statement
print datastore["office"]["parking"]["style"]
