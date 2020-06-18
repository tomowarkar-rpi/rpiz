import matplotlib.pyplot as plt
import pandas as pd

from common import BASE_DIR


def load_data(path):
    df = pd.read_csv(path, sep=" ", header=None)
    df.columns = ["date", "download", "upload"]

    df.date = pd.to_datetime(df.date, format="%Y%m%d%H")
    df.download = df.download.map(lambda x: round(x / 1e9, 2))
    df.upload = df.upload.map(lambda x: round(x / 1e9, 2))
    return df


def plt_fig(df):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(df.date, df.download, color="m")
    ax2.bar(df.date, df.upload, color="c", width=0.03)

    ax1.set_ylim([0, int(1.2 * max(df.download))])
    ax2.set_ylim([0, int(5 * max(df.upload))])

    ax1.set_ylabel("Download [GB]")
    ax2.set_ylabel("Upload [GB]")

    fig.autofmt_xdate(rotation=45)
    return fig


if __name__ == "__main__":
    from datetime import datetime

    dt = datetime.now().strftime("%Y%m")
    df = load_data(BASE_DIR + f"/cron/wifi/{dt}.txt")
    fig = plt_fig(df)
    fig.savefig(BASE_DIR + "/assets/wifi_img.png")

