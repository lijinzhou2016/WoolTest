datas = (
    '//*[@id="f65"]',
    '/html/body/div[4]/div[5]/div[2]/div[4]/div[1]/ul[3]/li[2]/ul/li[2]/a',
)


def get():
    import random
    return datas[random.randint(0, len(datas) - 1)]