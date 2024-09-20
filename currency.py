from bs4 import BeautifulSoup
from urllib.request import urlopen
import math

url = "https://currencyfreaks.com/convert/USD/ZAR/1.0"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

div_result = soup.find("div", class_='result')
result_text = div_result.text
number = float(
    result_text.split('=')[1].split('ZAR')[0].strip()
)

rounded_up = round(
    math.ceil(number * 100) / 100, 2
)

print(
    f"$1 = R{rounded_up}"
)


'''
In this modified code, after splitting the text at the "=" sign, 
we split the second element of the resulting list (index 1) 
at "ZAR" using the split() method. We then access the first 
element of the resulting list (index 0) to get the text between "=" 
and "ZAR". Finally, we use the strip() method to remove any 
leading or trailing whitespace from the extracted text.

The print(number) statement will output 17.6511833057298, 
which is the text between "=" and "ZAR" in the <span> tag.
'''

amount_to_change = float(
    input("Please enter an amount: $")
)
answer = amount_to_change * number
print(
    round(
        math.ceil(answer * 100) / 100, 2
    )
)