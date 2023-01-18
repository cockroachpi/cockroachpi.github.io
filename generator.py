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
    <style>* {background-color: "#420420"; color: "#696969"; font-family: "Montserrat";}</style>
</head>
<body>"""

z = """</body>
</html>"""

content_is_said_too_much = ""
for note in os.listdir(NOTES_PATH):
    with open(NOTES_PATH + note, "r") as note_file:
        content_is_said_too_much += markdown.markdown(note_file.read())

with open("index.html", "w") as page:
    page.write(a + content_is_said_too_much + z)

print ("gerenrantor is ending")