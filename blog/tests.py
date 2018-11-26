from django.test import TestCase

# Create your tests here.

#
#
# import datetime
#
# now=datetime.datetime.now().strftime("%Y-%m-%d")
#
# print(now)
# print(type(now))
#
#
# import json

# json.dumps(now)

# print("hello"[0:12])


from bs4 import BeautifulSoup


s=html_doc = """

<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<script>alert(123)</script>
"""



bs=BeautifulSoup(s,"html.parser")
# print(bs.text)



# print(bs.find_all("a"))
#
# for tag in bs.find_all("a"):
#     print(tag.get("href"))

# print(bs.find_all())


for tag in bs.find_all():

    print(tag.name)

    if tag.name in ["script","link"]:
        tag.decompose()

print(str(bs))














