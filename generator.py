#!/usr/local/python/3.10.4/bin/python
import os
import re
import pytz
import markdown
import datetime

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
        background-color: black;/*#4564b9;*/ 
        color: white; 
        font-family: "Montserrat";
        margin-left: 30px;
        margin-right: 50px;
        margin-top: 3px;
        }
        .chrzanic_notki {
            border-bottom: 1px dashed white;
        }
        h3 {
            font-size: 15px;
        }
    </style>
</head>
<body>
    <h1>a teraz będę słuchał</h1>
"""

z = """</body>
</html>"""

def warsaw_time():
    date = datetime.datetime.now(pytz.timezone('Europe/Warsaw'))
    return f"{str(date.day).zfill(2)}.{str(date.month).zfill(2)}.{date.year}\n"

def compile_post(path):
    with open(path, 'r+', encoding='utf-8') as file:
        #if(re.search(r'\d{2}\.\d{2}\.\d{4}', file.read())):
        #    text = file.read()
        #    file.seek(0,0)
        #    file.write(warsaw_time())
        #    file.write(text)
        return """\t<div class="chrzanic_notki">""" + "".join(markdown.markdown(file.read()).split("\n")) + "</div>\n"

content_is_said_too_much = ""
posty = os.listdir(NOTES_PATH)
posty.sort(key = lambda x: int(x[:-3]))
posty.reverse()
print(posty)
for note in posty:
    content_is_said_too_much += compile_post(NOTES_PATH+note)

with open ("index.html", "w", encoding='utf-8') as page:
    page.write(a + content_is_said_too_much + z)

print ("gerenrantor is ending")