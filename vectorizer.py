"""
TinyVectorizer - 意味ベースの文書ベクター化処理
"""

from sentence_transformers import SentenceTransformer


_model = None


def _get_model() -> SentenceTransformer:
    """モデルを遅延ロードして返す"""
    global _model
    if _model is None:
        _model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return _model


def vectorize(text: str) -> list[float]:
    """
    文字列をセマンティックベクトルに変換する

    Args:
        text: ベクター化する文字列

    Returns:
        384次元の埋め込みベクトル（多言語対応）
    """
    model = _get_model()
    embedding = model.encode(text)
    return embedding.tolist()


def similarity(text1: str, text2: str) -> float:
    """
    2つの文字列の意味的類似度を計算する

    Args:
        text1: 比較する文字列1
        text2: 比較する文字列2

    Returns:
        コサイン類似度（0〜1の値、1に近いほど類似）
    """
    from sentence_transformers import util

    model = _get_model()
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)
    return float(util.cos_sim(emb1, emb2)[0][0])


def find_most_similar(query: str, documents: list[str]) -> tuple[int, str, float]:
    """
    クエリに最も意味的に近い文書を見つける

    Args:
        query: 検索クエリ
        documents: 検索対象の文書リスト

    Returns:
        (インデックス, 文書, 類似度スコア)のタプル
    """
    from sentence_transformers import util

    model = _get_model()
    query_emb = model.encode(query)
    doc_embs = model.encode(documents)

    similarities = util.cos_sim(query_emb, doc_embs)[0]
    best_idx = int(similarities.argmax())

    return best_idx, documents[best_idx], float(similarities[best_idx])


if __name__ == "__main__":
    docs = [
        "猫が庭で遊んでいる",
        "犬が公園を走っている",
        "プログラミングは楽しい",
        "機械学習でデータを分析する",
    ]

    query = "ペットが外で遊ぶ"
    idx, doc, score = find_most_similar(query, docs)

    print(f"Query: {query}")
    print(f"Most similar: {doc} (score: {score:.4f})")
