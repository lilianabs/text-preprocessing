import re

def extract_hashtags(txt: str):
    """Extracts hastags from a given string

    Args:
        txt (str): Text 

    Returns:
        list: List that contains all hashtags
    """
    return re.findall(r'(?<!\S)#\S+|\S+#(?!\S)', txt)