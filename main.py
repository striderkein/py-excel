import os
import shutil
from datetime import datetime

def main():
  dist = os.path.expanduser('~/Documents/daily_repo/dist')
  todayDate = datetime.now().strftime("%Y%m%d")
  templateFilePath = './template/YYYYMMDD_業務日報_.xlsx'
  distFilePath = os.path.join(dist, f"{ todayDate }_業務日報_.xlsx")

  # template からコピーして新規ファイル作成
  shutil.copyfile(templateFilePath, distFilePath)

if __name__ == '__main__':
  main()
