# Image Scraper - 日本語版

Google Images から各種キーワードに基づき画像を自動ダウンロードする汎用的な Python ツール（Selenium 使用）。

## 機能

- テキストファイル（`items_list.txt`）から検索キーワードを読み込む。
- 各キーワードごとにフォルダを作成し、画像を分類。
- （オプションでキーワードを追加）ヘッドレスモードで Google 画像検索を実行。
- 指定枚数の画像をダウンロードし、JPEG 形式に変換。

## 前提条件

- Python 3.8 以上
- Google Chrome ブラウザがインストールされていること

## インストール手順

1. リポジトリをクローン：

   ```bash
   git clone https://github.com/<your-username>/image-scraper.git
   cd image-scraper
   ```

2. 依存パッケージをインストール：

   ```bash
   pip install -r requirements.txt
   ```

3. 検索キーワードを用意：
   プロジェクトルートに`items_list.txt`を作成し、1 行に 1 キーワードを記載。
   `#`で始まる行はコメント、1 文字の行はセクションフォルダ。

## 使い方

```bash
python main.py --input items_list.txt --output images --max-images 30 --suffix "underwater"
```

- `--input`: キーワードリストファイルのパス
- `--output`: 画像保存先ディレクトリ
- `--max-images`: 1 キーワードあたりの最大ダウンロード枚数（デフォルト 30）
- `--suffix`: 検索語に追加で付けるキーワード（省略可）

## プロジェクト構成

- `main.py`: メインスクリプト
- `requirements.txt`: Python ライブラリ依存
- `.gitignore`: Git 無視設定
- `README.md`: 英語版 README
- `README_ja.md`: 日本語版 README

```

```
