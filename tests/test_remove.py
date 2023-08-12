from src.text_preprocessing.remove import remove_hashtags
from src.text_preprocessing.remove import remove_user_mentions
from src.text_preprocessing.remove import remove_url


def test_remove_hashtags():
    txt = "This text contains hashtags #be-happy and #test"
    txt_without_hashtags = "This text contains hashtags and "
    txt_removed_hashtags = remove_hashtags(txt)

    assert txt_without_hashtags == txt_removed_hashtags


def test_remove_user_mentions():
    txt = "This text contains @user, @second_user, and @user3  mentions"
    txt_without_user_mentions = "This text contains , , and mentions"
    txt_removed_user_mentions = remove_user_mentions(txt)

    assert txt_without_user_mentions == txt_removed_user_mentions


def test_remove_url():
    txt = """This text contains url https://www.google.com/"""
    txt_without_urls = "This text contains url "
    txt_removed_urls = remove_url(txt)

    assert txt_without_urls == txt_removed_urls
