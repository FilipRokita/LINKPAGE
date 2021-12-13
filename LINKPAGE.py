#LINKPAGE
#Filip Rokita
#www.filiprokita.com

#writing/reading settings.py
while True:
	print("\n")
	print("CHOOSE")
	print("1. Create new link page configuration")
	print("2. Load configuration from settings.py")
	choice = input("CHOICE: ")
	if choice == "1":
		#input site settings
		author = input("AUTHOR: ")
		description = input("DESCRIPTION: ")
		fontcolor = input("FONT COLOR: ")
		itembackgroundcolor = input("ITEM BACKGROUND COLOR: ")
		backgroundcolor = input("BACKGROUND COLOR: ")
		#write site settings
		settings = open("settings.py", "w")
		settingscontent = """author = """+'"'+author+'"'+"""
description = """+'"'+description+'"'+"""
fontcolor = """+'"'+fontcolor+'"'+"""
itembackgroundcolor = """+'"'+itembackgroundcolor+'"'+"""
backgroundcolor = """+'"'+backgroundcolor+'"'+""""""
		settings.write(settingscontent)
		settings.close()
		break
	elif choice == "2":
		try:
			from settings import *
			break
		except:
			print("\n" * 100)
			print("File settings.py does not exist! Try again.")
			print("\n")
	else:
		print("\n" * 100)
		print("This choice is not available! Try again.")





#writing/reading links.py
while True:
	print("\n")
	print("CHOOSE")
	print("1. Create new links")
	print("2. Load existing links from links.py")
	choice = input("CHOICE: ")
	if choice == "1":
		while True:
			numberoflinks = int(input("NUMBER OF LINKS: "))
			if numberoflinks >= 1 and numberoflinks <=100:
				linktitle = [None] * (numberoflinks + 1)
				link = [None] * (numberoflinks + 1)
				for i in range(1, numberoflinks + 1):
					linktitle[i] = input("LINK TITLE "+str(i)+": ")
					link[i] = input("LINK "+str(i)+": ")
					int(i)
				links = open("links.py", "w")
				linkscontent = """linktitle = """+str(linktitle)+"""
link = """+str(link)+""""""
				links.write(linkscontent)
				links.close()
				break
			else:
				print("\n" * 100)
				print("Number of links must be between 1 and 100! Try again.")
				print("\n")
		break
	elif choice == "2":
		try:
			from links import *
			break
		except:
			print("\n" * 100)
			print("File links.py does not exist! Try again.")
			print("\n")
	else:
		print("\n" * 100)
		print("This choice is not available! Try again.")
		print("\n")





#formatting links for <div id="links">
divcontent = ""
for i in range(1, len(link)):
	divcontent = divcontent + """
			<div id="link">
				<h2>"""+str(linktitle[i])+"""</h2>
	    		<a href="""+'"'+str(link[i])+'"'+""" class="button"><b>CLICK</b></a>
			</div>"""
divcontent = divcontent.strip()





#creating index.html
index = open("index.html", "w")
indexcontent = """<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>"""+author+" - LINKPAGE"+"""</title>
		<meta name="description" content="""+'"'+description+'"'+"""/>
		<meta name="keywords" content="""+'"'+author+", "+"linkpage"+", "+"links"+'"'+"""/>
		<meta name="author" content="""+'"'+author+'"'+"""/>
		<link rel="stylesheet" href="style.css"/>
		<script src="script.js"></script>
	</head>
	<body>
	    <header>
		    <h1>"""+author+"""</h1>
		    <p>"""+description+"""</p>
		</header>
		<div id="content">
			"""+divcontent+"""
		</div>
	</body>
</html>"""
index.write(indexcontent)
index.close()





#creating style.css
style=open("style.css", "w")
stylecontent = """body {
    font-family: arial;
    text-align: center;
    background-color: """+backgroundcolor+""";
}
header {
	margin: 50px;
    padding: 30px;
    font-size: 20px;
    color: """+fontcolor+""";
    background: """+itembackgroundcolor+""";
	border-radius: 50px;
}
#link {
    margin: 0px 100px 100px 100px;
}
h2 {
    padding: 10px;
    margin: 0px 20% 40px 20%;
    color: """+fontcolor+""";
    background-color: """+itembackgroundcolor+""";
    border-radius: 50px;
}
.button {
    padding: 10px 30px;
    cursor: pointer;
    color: """+fontcolor+""";
    text-decoration: none;
    background-color: """+itembackgroundcolor+""";
    border-radius: 50px;
}"""
style.write(stylecontent)
style.close()





#creating script.js
script = open("script.js", "w")
scriptcontent = """"""
script.write(scriptcontent)
script.close()
