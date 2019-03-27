import requests
import proxys
import wools

rs = response = requests.get("http://www.qingool.com:8000/?protocol=1&country=%E5%9B%BD%E5%86%85").json()
print(rs)

# proxies = {
#     "https": requests.get("http://118.24.52.95:5010/get").text
# }
#
# rs = requests.get("http://www.baidu.com", proxies=proxies, timeout=5)
# print(rs.text)