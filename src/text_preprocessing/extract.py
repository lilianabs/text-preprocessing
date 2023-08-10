import re


def extract_hashtags(txt: str):
    """Extracts hastags from a given text

    Args:
        txt (str): Text

    Returns:
        list: List that contains all hashtags
    """
    return re.findall(r"(?<!\S)#\S+|\S+#(?!\S)", txt)


def extract_user_mentions(txt: str):
    """Extracts user mentions from a given text

    Args:
        txt (str): Text

    Returns:
        list: List that contains all user mentions
    """
    return re.findall(r"@\w+", txt)


def extract_url(txt: str):
    """Extracts url's from a given text

    Args:
        txt (str): Text
    Returns:
        list: List that contains urls
    """
    return re.findall(r"https?://\S+", txt)
