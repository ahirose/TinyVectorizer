# TinyVectorizer

セマンティック検索と文書類似度計算のための軽量なPython文字列ベクトル化ライブラリ

## 📝 概要

TinyVectorizerは、文字列を意味ベースのベクトルに変換し、文書間の意味的類似度を計算するためのシンプルなライブラリです。多言語対応のトランスフォーマーモデルを使用し、日本語や英語などの言語で高精度な意味理解を実現します。

## ✨ 主な機能

- **ベクトル化**: 文字列を384次元のセマンティックベクトルに変換
- **類似度計算**: 2つの文字列間の意味的類似度を計算（コサイン類似度）
- **類似文書検索**: 複数の文書から最も類似した文書を検索
- **多言語対応**: 日本語、英語など50以上の言語に対応
- **効率的**: モデルの遅延ロードで初回起動時のみロード

## 🚀 インストール

```bash
pip install sentence-transformers
```

## 💡 使い方

### 基本的な使い方

```python
from vectorizer import vectorize, similarity, find_most_similar

# 1. 文字列をベクトル化
vector = vectorize("機械学習は面白い")
print(f"ベクトル次元: {len(vector)}")  # 384

# 2. 2つの文字列の類似度を計算
score = similarity("猫が好き", "犬が好き")
print(f"類似度: {score:.4f}")  # 0.8程度

# 3. 最も類似した文書を検索
documents = [
    "猫が庭で遊んでいる",
    "犬が公園を走っている",
    "プログラミングは楽しい",
    "機械学習でデータを分析する"
]
query = "ペットが外で遊ぶ"
idx, doc, score = find_most_similar(query, documents)
print(f"最も類似: {doc} (スコア: {score:.4f})")
```

### デモの実行

```bash
python vectorizer.py
```

実行結果の例:
```
Query: ペットが外で遊ぶ
Most similar: 猫が庭で遊んでいる (score: 0.7234)
```

## 🔧 技術仕様

- **モデル**: `paraphrase-multilingual-MiniLM-L12-v2`
- **ベクトル次元**: 384次元
- **フレームワーク**: Sentence Transformers（Hugging Face）
- **類似度指標**: コサイン類似度

## 📚 API リファレンス

### `vectorize(text: str) -> list[float]`
文字列を384次元のベクトルに変換します。

**引数:**
- `text`: ベクトル化する文字列

**戻り値:**
- 384次元の埋め込みベクトル（リスト）

### `similarity(text1: str, text2: str) -> float`
2つの文字列間の意味的類似度を計算します。

**引数:**
- `text1`: 比較する文字列1
- `text2`: 比較する文字列2

**戻り値:**
- コサイン類似度（0〜1、1に近いほど類似）

### `find_most_similar(query: str, documents: list[str]) -> tuple[int, str, float]`
クエリに最も意味的に近い文書を検索します。

**引数:**
- `query`: 検索クエリ
- `documents`: 検索対象の文書リスト

**戻り値:**
- `(インデックス, 文書, 類似度スコア)` のタプル

## 🎯 ユースケース

- セマンティック検索エンジン
- 文書分類・クラスタリング
- 重複文書検出
- FAQ自動マッチング
- チャットボットの意図理解

## 📄 ライセンス

このプロジェクトはオープンソースです。
