from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# Finding the page title
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

# Finding the name
pattern = "<h2>.*?</h2>"
match_results = re.search(pattern, html, re.IGNORECASE)
name = match_results.group()
name = re.sub("<.*?>", "", name)

print(
    title, "\n",
    name
)

# Finding the color
color_pattern = "Color:.*"

match = re.search(color_pattern, html, re.IGNORECASE)
if match:
    print(
        match.group()
    )
else:
    print(
        "no match found"
    )