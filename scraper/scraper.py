from bs4 import BeautifulSoup
import requests


source_code = requests.get("https://quotes.toscrape.com/").text
contents = BeautifulSoup(source_code,"lxml")
# print(contents.prettify()) # this statement prints the HTML is a proper way

# the following code is used when the html file is present in your folder
# with open("data/sample-1.html") as f:
#     contents = BeautifulSoup(f,"lxml")

print ("\nDisplaying all the quotes from https://quotes.toscrape.com/ === \n")
for quotes in contents.find_all("div", class_="quote"):
    reqquotes = quotes.span.text.replace('"', " ")
    print(reqquotes[1:-1]," = ", quotes.small.text)


books_code = requests.get("https://books.toscrape.com/").text
books_content = BeautifulSoup(books_code,"lxml")
# book_title = books_content.find("article", class_="product_pod")
# print (book_title.h3.a.get("title"))

# book_title = books_content.find("div", class_="image_container")
# print (book_title.img.get('alt'))

print ("\nDisplaying the names of all the books === \n")
for b in books_content.find_all("article", class_="product_pod"):
    book_title = b.div.a.img.get('alt')
    book_price = b.find("p", class_="price_color")
    print (book_title, " = ", book_price.text[1:])

