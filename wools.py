datas = (
    "https://yeah.qq.com/s.html?q=259745",
    "https://123.sogou.com/?22646-6101",
    "https://123.sogou.com/?22646-6106",
    "https://123.sogou.com/?22646-6105"
)


def get():
    import random
    return datas[random.randint(0, len(datas) - 1)]


def get_all():
    return datas