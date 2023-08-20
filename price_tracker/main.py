from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://camelcamelcamel.com/product/B0815XFSGK"
BUY_PRICE = 150
EMAIL = ""
PASSWORD = ""

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(url=URL, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
price = soup.find(class_="green").get_text()

if price <= BUY_PRICE:
    message = f"The item is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )