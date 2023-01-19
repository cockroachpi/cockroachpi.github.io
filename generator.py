#!/usr/local/python/3.10.4/bin/python
import os
import markdown

print ("generator iis strarting")

NOTES_PATH = "./notes/"

a = """<!DOCTYPE html>
<html>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap" rel="stylesheet">
    <style>
        body {
        background-color: #4564b9; 
        color: white; 
        font-family: "Montserrat";
        margin-left: 30px;
        margin-right: 50px;
        margin-top: 3px;
        }
        chrzanic_notki {
            border-bottom: 2px solid white;
        }
    </style>
</head>
<body>
    <h1>bunt maszyn w końcu nadejdzie</h1>"""

z = """</body>
</html>"""

def compile_post(path):
    with open(path, 'r') as file:
        return """<div class="chrzanic_notki">""" + "".join(markdown.markdown(file.read())) + "</div>"

content_is_said_too_much = ""
posty = os.listdir(NOTES_PATH)
posty.sort()
posty.reverse()
print(posty)
for note in posty:
    content_is_said_too_much += compile_post(NOTES_PATH+note)

with open ("index.html", "w") as page:
    page.write(a + content_is_said_too_much + z)

print ("gerenrantor is ending")