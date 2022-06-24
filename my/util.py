from typing import Union, List

def hoge():
  return 'hoge'

# def convCell(address: Union[List[int], str]) -> Union[List[int], str]:
#   converted = None
#   if type(address) == List[int]:
#     converted = f"{ address[0] - 1 + 65 }{ address[1] }"
#   return converted

def convCell(address: str) -> dict:
  """Excelのセルを表す'A1'などの文字列を{ row, col }形式の dict に変換して返却する。

  Args:
    address: Excelのセルを表す'A1'などの文字列

  Returns:
    プロパティとして row, col を持つ dict
    example:
    { row: 行番号を表す数値, col: 列番号を表す数値 }
  """
  converted = dict()

  # 引数の1文字めについて下記の処理を行い、'A' -> 65 -> 1 となる変換を実現する。
  # 1 Unicode コードポイントを表す整数に変換
  # 2. 1 の処理結果に対して 64 を減じる
  converted['col'] = ord(address[0:1]) - 64
  # 引数の2文字めは int への変換のみ
  converted['row'] = int(address[1:2])
  return converted

# if __name__ == '__main__':
  # util()
