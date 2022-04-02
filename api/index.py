import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3770.100 Safari/537.36"
}
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    html_head = """
    <html>
    <head>
    <title>heyBox</title>
    </head>
    <body>
    <h3>本站数据来自互联网，仅为方便玩家使用！不得用于任何商业用途。如有侵权请告知：TTATT</h3>
    """
    html_end = """
    </body>
    </html>
    """
    html_body = ""

    heyUrl = "https://api.xiaoheihe.cn/game/h5_activity/common_team/data?appid=1085660&need_list=1&offset=0&limit=30"
    _response = requests.get(heyUrl, headers=headers)
    data = json.loads(_response.text)

    trimData = data["result"]["data_list"]
    for singleData in trimData:
        try:
            nickName = singleData["user"]["username"]
            nickName = "<b>" + nickName + "</b>"
        except Exception:
            nickName = "None"
        try:
            description = singleData["description"]
            description = description.replace("Document", "")
            description = description.replace("不限", "")
            description = description.replace("要求语音", "<b>要求语音</b>")
            description = description.replace("ID", "<b> ID：</b>")
            description = description.replace("光等", "<b> 要求光等：</b>")
        except Exception:
            description = "None"
        try:
            title = singleData["team_data"]["team_text"]
        except Exception:
            title = "None"
        try:
            shareUrl = singleData["share_url"]
        except Exception:
            shareUrl = "None"

        html_body += '<p>🤺{}喊话：{} 🍭 {} 🔗<a target="_blank" href="{}">帖子</a></p>'.format(
            nickName, title, description, shareUrl
        )

    return html_head + html_body + html_end


if __name__ == "__main__":
    app.run()
