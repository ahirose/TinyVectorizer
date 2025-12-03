"""
TinyVectorizer - 最も簡単な文字列ベクター化処理
"""


def vectorize(text: str) -> list[int]:
    """
    文字列を数値ベクトルに変換する

    各文字のUnicodeコードポイントをリストとして返す

    Args:
        text: ベクター化する文字列

    Returns:
        各文字のUnicodeコードポイントのリスト
    """
    return [ord(char) for char in text]


if __name__ == "__main__":
    sample = "Hello, World!"
    result = vectorize(sample)
    print(f"Input: {sample}")
    print(f"Vector: {result}")
