# py-excel

## requires
- Python ^3.7.0

## How to install
```
./install.sh
```

## How to setup
step-1
```
cp .env.example .env
```

step-2: modify `.env` according to your environment.

- TARGET_SHEET: 出力先シート名（テンプレートとなる「YYYYMMDD_業務日報_.xlsx」に変更がない限り編集不要）
- CURRENT_USER_NAME: 日報提出者（you!）の氏名
- GIT_REPOSITORIES: Git リポジトリをクローンしてきてる親ディレクトリ
- DIST: 日報の出力先ディレクトリ

## How to use
```
python main.py
```

## available scripts
### import 文の整理
```
pipenv run isort
```
