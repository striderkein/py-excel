import os
import shutil
from datetime import datetime

dist = os.path.expanduser('~/Documents/daily_repo/dist')
todayDate = today = datetime.now().strftime("%Y%m%d")
templateFilePath = './template/YYYYMMDD_業務日報_.xlsx'
distFilePath = os.path.join(dist, f"{ todayDate }_業務日報_.xlsx")

# template からコピーして新規ファイル作成
shutil.copyfile(templateFilePath, distFilePath)
