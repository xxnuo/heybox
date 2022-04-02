import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3770.100 Safari/537.36"
}
import json
from flask import Flask

app = Flask(__name__)


class heyBox:
    # 组合URL
    def __GetUrl(
        self,
        url_base="https://api.xiaoheihe.cn/bbs/app/topic/feeds",
        url_limit=30,
        url_topic_id=65410,
        url_cate_id=21,
        url_offset=0,
    ):
        url = "{}?topic_id={}&cate_id={}&offset={}&limit={}".format(
            url_base, url_topic_id, url_cate_id, url_offset, url_limit
        )
        return url

    def __GetJsonData(self, url):
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return data["result"]["links"]

    # pubilc = = = = = = =

    def __init__(self):
        self.apiUrl = self.__GetUrl()
        self.jsonData = {}
        self.__updated = False

    def Update(self):
        self.jsonData = self.__GetJsonData(self.apiUrl)
        self.__updated = True

    def Updated(self):
        return self.__updated

    def Info(self, id=0):
        try:
            singleData = self.jsonData[id]
        except:
            return "", ""
        share_url = singleData["share_url"]
        title = singleData["title"]
        description = singleData["description"]
        userName = self.jsonData[id]["user"]["username"]
        return (userName, title, description, share_url)

    def InfoAll(self):
        allData = []
        for i in self.jsonData:
            number = self.jsonData.index(i)
            allData.append(self.Info(number))
        return allData


@app.route("/")
def index():
    html_head = """
    <html>
    <head>
    <title>heyBox</title>
    </head>
    <body>
    <h2>刷新即可获取最新数据，按最新回复展示。</h2>
    """
    html_end = """
    </body>
    </html>
    """
    html_body = ""

    heyBox.Update()
    # print("请求:" + heyBox.apiUrl)
    for i in heyBox.InfoAll():
        # print(i)
        html_body += '&#9830;昵称：《{}》&#9830;标题：《{}》&#9830;描述：《{}》&#9830;<a target="_blank" href="{}">链接</a></br>'.format(
            i[0], i[1], i[2], i[3]
        )
    return html_head + html_body + html_end


if __name__ == "__main__":
    heyBox = heyBox()
    app.run()
