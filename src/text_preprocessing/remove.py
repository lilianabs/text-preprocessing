import re


def remove_hashtags(txt: str):
    """Removes hastags from a given text

    Args:
        txt (str): Text

    Returns:
        txt (str): Text without hashtags
    """
    txt_without_hashtags = re.sub(r"(?<!\S)#\S+|\S+#(?!\S)", "", txt)
    return re.sub(" +", " ", txt_without_hashtags)


def remove_user_mentions(txt: str):
    """Removes user mentions from a given text

    Args:
        txt (str): Text

    Returns:
        txt (str): Text without user mentions
    """
    txt_without_user_mentions = re.sub(r"@\w+", "", txt)
    return re.sub(" +", " ", txt_without_user_mentions)


def remove_url(txt: str):
    """Extracts url's from a given text

    Args:
        txt (str): Text
    Returns:
        list: List that contains urls
    """
    txt_without_urls = re.sub(r"https?://\S+", "", txt)
    return re.sub(" +", " ", txt_without_urls)
