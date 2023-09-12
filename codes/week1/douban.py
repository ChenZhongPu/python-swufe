import requests
from bs4 import BeautifulSoup
import os


def download_image():
    url = "https://book.douban.com/chart?subcat=all&icn=index-topchart-popular"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    all_books = soup.find_all("li", class_="media clearfix")
    if not os.path.exists("img"):
        os.mkdir("img")
    for book in all_books:
        img_url = book.find("img")["src"]
        img_name = img_url.split("/")[-1]
        data = requests.get(img_url, stream=True)
        print(f"Download {img_name} ...")
        with open("img/" + img_name, "wb") as f:
            f.write(data.content)


if __name__ == "__main__":
    download_image()
