from typing import Union, List

def hoge():
  return 'hoge'

# def convCell(address: Union[List[int], str]) -> Union[List[int], str]:
#   converted = None
#   if type(address) == List[int]:
#     converted = f"{ address[0] - 1 + 65 }{ address[1] }"
#   return converted

def convCell(address: str) -> List[int]:
  # converted = None
  # if type(address) == List[int]:
  # 'A' -> 65 -> 1 となる変換
  hoge = ord(address[0:1]) - 64
  fuga = int(address[1:2])
  # converted = f"{ hoge }{ fuga }"
  converted = [hoge, fuga]
  return converted

# if __name__ == '__main__':
  # util()
