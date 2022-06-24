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


  repo = 'art-lesson'
  # command = f'cd ~/dev/{ repo };git log --oneline --branches --reverse --date=short --author=\"$(git config user.name)\" --pretty=format:\"- [%ad] %h: %s\" --since=\"last day\"'
  command = f'cd ~/dev/{ repo };git log --oneline --branches --reverse --date=short --author=\"$(git config user.name)\" --pretty=format:\"%h,%s\" --since=\"last day\"'
  stream = os.popen(command)
  logs = stream.read().split('\n')

  cell = util.convCell("B1")
  startCell = util.convCell("A6")
  endCell = util.convCell("B6")
  asanaTaskNameCell = util.convCell("D6")
  detailCell = util.convCell("E6")
  remarksCell = util.convCell("F6")
  startRow = detailCell['row']

  # print(f"cell['row']:{ cell['row'] }, cell.['col']:{ cell['col'] }")
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

  for i, log in enumerate(logs):
    print(f'{ log }')
    lo = log.split(',')
    sheet.cell(row=startRow + i, column=detailCell['col']).value = lo[1]
    sheet.cell(row=startRow + i, column=remarksCell['col']).value = lo[0]

  wb.save(distFilePath)
  wb.close()

if __name__ == '__main__':
  main()
