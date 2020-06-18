import streamlit as st

from common import BASE_DIR


def load_date():
    from PIL import Image

    image = Image.open(BASE_DIR + "/assets/wifi_img.png")
    st.image(image, caption="wifi status", use_column_width=True)


def get_3d_wifi():
    import re
    import requests

    url = "http://speedwifi-next.home/api/monitoring/statistics_3days"
    r = requests.get(url)
    if not r.ok:
        st.error("connection not found")
        return
    ttd = re.findall("<ToTodayDownload>(\d+)", r.text)[0]

    st.write("{} GB".format(round(int(ttd) / 1e9, 2)))


if __name__ == "__main__":
    st.title("Hello RPIZ")
    get_3d_wifi()
    load_date()

