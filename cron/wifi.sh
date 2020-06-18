#!/bin/bash
# @(#) speed wifi データ通信量を保存
PJT_DIR=$(
    cd $(dirname $0)
    pwd
)

# ディレクトリがなければ作成
mkdir -p ${PJT_DIR}/wifi

# ファイルは月毎に更新
dt=$(date +%Y%m)
TAR_FILE=${PJT_DIR}/wifi/${dt}.txt

touch ${TAR_FILE}

echo $(date +%Y%m%d%H &&
    curl -s http://speedwifi-next.home/api/monitoring/month_statistics |
    sh $(dirname ${PJT_DIR})/scripts/xml_parse.sh |
        grep -e CurrentMonth |
        cut -d" " -f2) >>${TAR_FILE}

