import json
from markdown2 import markdown

config = open("config.json", "r")	

configurated = json.load(config)	

stuff = open("pages/index.html", "r")	

data = stuff.read()	
data = data.replace("///site", configurated["site"])	
stuff = open("pages/index.html", "w")	
stuff.write(data)	
stuff.close()

stuff = open("config/main.md", r)

d = stuff.read()
d = markdown(d)
stuff.close()
stuff = open("pages/index.html", w+)
data = stuff.read()
data = data.replace("{{body}}",d)
data = data.replace("{{site}}",configurated["site"])
data = data.replace("{{issue-number}}",configurated["issue-number"])
stuff.write(data)
stuff.close()
