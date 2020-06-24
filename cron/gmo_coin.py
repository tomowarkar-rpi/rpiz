from datetime import datetime
import requests
import json


url = "https://api.coin.z.com/public/v1/ticker?symbol=BTC_JPY"
r = requests.get(url)
j = json.loads(r.text)
[data] =  j.get("data")
file = "/home/pi/cron/gmo_coin/"
file += datetime.strptime(data.get("timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y%m%d") + ".txt"
text = "{} {} {}\n".format(*map(lambda x: data.get(x), ["timestamp", "ask","bid"]))
with open(file, mode="a") as f:
    f.write(text)
