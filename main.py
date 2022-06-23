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

  cell = util.convCell("B1")
  startCell = util.convCell("A6")
  endCell = util.convCell("B6")
  asanaTaskNameCell = util.convCell("D6")
  detailCell = util.convCell("E6")
  remarksCell = util.convCell("F6")
  print(f"cell['row']:{ cell['row'] }, cell.['col']:{ cell['col'] }")
  # insert to cell: A1
  # op.1: with positional arguments
  # sheet.cell(row=1, column=2).value = todayDateSeparateWithSlash
  # op.2: without positional arguments
  # sheet.cell(1, 2).value = todayDateSeparateWithSlash
  sheet.cell(row=cell['row'], column=cell['col']).value = todayDateSeparateWithSlash
  sheet.cell(row=2, column=2).value = myName
  sheet.cell(row=startCell['row'], column=startCell['col']).value = "10:00"
  sheet.cell(row=endCell['row'], column=endCell['col']).value = "19:00"
  sheet.cell(row=asanaTaskNameCell['row'], column=asanaTaskNameCell['col']).value = "some task"
  sheet.cell(row=detailCell['row'], column=detailCell['col']).value = "working detail"
  sheet.cell(row=remarksCell['row'], column=remarksCell['col']).value = "many bugs exists!"

  wb.save(distFilePath)
  wb.close()

if __name__ == '__main__':
  main()
