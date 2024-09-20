from bs4 import BeautifulSoup
from urllib.request import urlopen
import math


def round_up(num):
    return round(
        math.ceil(num * 100) / 100, 2
    )


url = "https://currencyfreaks.com/convert/USD/ZAR/1.0"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

div_result = soup.find("div", class_='result')
result_text = div_result.text
number = float(
    result_text.split('=')[1].split('ZAR')[0].strip()
)

rounded_up = round_up(number)

amount_to_change = float(
    input("Please enter an amount: $")
)
answer = amount_to_change * number
print(
    f"$1 = R{rounded_up} \n${amount_to_change} = R{round_up(answer)}"
)
