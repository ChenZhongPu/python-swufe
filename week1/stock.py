import requests


def get_stock_info(stock_id):
    r = requests.get(f"https://sqt.gtimg.cn/q={stock_id}").text
    stock = r[r.index('"') + 1 : r.rindex('"')].split("~")
    name = stock[1]
    price = float(stock[3])
    stock_info = {
        "name": name,
        "price": price,
    }
    return stock_info


if __name__ == "__main__":
    stock_info = get_stock_info("sh600000")
    print(f"{stock_info['name']}的当前价格为{stock_info['price']}")
