import os
import shutil
from typing import List
from datetime import datetime
from dotenv import load_dotenv
import openpyxl

from my import util

def main():
  load_dotenv()
  myName = os.getenv('CURRENT_USER_NAME_JP')

  # print(util.convCell(List[1, 2])) # NG

  dist = os.path.expanduser('~/Documents/daily_repo/dist')
  todayDate = datetime.now().strftime("%Y%m%d")
  todayDateSeparateWithSlash = datetime.now().strftime("%Y/%m/%d")
  templateFilePath = './template/YYYYMMDD_業務日報_.xlsx'
  distFilePath = os.path.join(dist, f"{ todayDate }_業務日報_.xlsx")
  targetSheet = '業務報告書'

  # template からコピーして新規ファイル作成
  shutil.copyfile(templateFilePath, distFilePath)

  # ディレクトリを指定してワークブック（いわゆる Excel ファイル）を開く
  wb = openpyxl.load_workbook(distFilePath)
  sheet = wb[targetSheet]

  # for DEBUG
  # 読み込み: OK
  # value = sheet.cell(row=1, column=1).value
  # print(value)

  # 書き込み: B1 に '<YYYY/MM/DD>' と書き込む
  cell = util.convCell("B1")
  startCell = util.convCell("A6")
  endCell = util.convCell("B6")
  asanaTaskNameCell = util.convCell("D6")
  detailCell = util.convCell("E6")
  remarksCell = util.convCell("F6")
  print(f"cell[0]:{ cell[0] }, cell[1]:{ cell[1] }")
  # insert to cell: A1
  # op.1: with positional arguments
  # sheet.cell(row=1, column=2).value = todayDateSeparateWithSlash
  # op.2: without positional arguments
  # sheet.cell(1, 2).value = todayDateSeparateWithSlash
  sheet.cell(cell[1], cell[0]).value = todayDateSeparateWithSlash
  sheet.cell(row=2, column=2).value = myName
  sheet.cell(startCell[1], startCell[0]).value = "10:00"
  sheet.cell(endCell[1], endCell[0]).value = "19:00"
  sheet.cell(asanaTaskNameCell[1], asanaTaskNameCell[0]).value = "some task"
  sheet.cell(detailCell[1], detailCell[0]).value = "working detail"
  sheet.cell(remarksCell[1], remarksCell[0]).value = "many bugs exists!"

  wb.save(distFilePath)
  wb.close()

if __name__ == '__main__':
  main()
