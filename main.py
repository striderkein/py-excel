import os
import shutil
from datetime import datetime
import openpyxl

def main():
  dist = os.path.expanduser('~/Documents/daily_repo/dist')
  todayDate = datetime.now().strftime("%Y%m%d")
  templateFilePath = './template/YYYYMMDD_業務日報_.xlsx'
  distFilePath = os.path.join(dist, f"{ todayDate }_業務日報_.xlsx")

  # template からコピーして新規ファイル作成
  shutil.copyfile(templateFilePath, distFilePath)

  wb = openpyxl.load_workbook(distFilePath)
  sheet = wb['業務報告書']

  # 読み込み: OK
  value = sheet.cell(row=1, column=1).value
  print(value)

  wb.close()

if __name__ == '__main__':
  main()
