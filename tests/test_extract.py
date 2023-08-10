from src.text_preprocessing.extract import extract_hashtags
from src.text_preprocessing.extract import extract_user_mentions
from src.text_preprocessing.extract import extract_url


def test_extract_hashtag():
    txt = "This text contains hashtags #be-happy and #test"
    hashtags_from_txt = ["#be-happy", "#test"]
    extracted_hashtags = extract_hashtags(txt)

    assert extracted_hashtags == hashtags_from_txt


def test_extract_user_mentions():
    txt = "This text contains @user, @second_user, and @user3  mentions"
    user_mentions_from_txt = ["@user", "@second_user", "@user3"]
    extracted_user_mentions = extract_user_mentions(txt)

    assert extracted_user_mentions == user_mentions_from_txt


def test_extract_url():
    txt = """This text contains url https://www.google.com/ 
          and https://www.youtube.com/"""
    urls_from_txt = ["https://www.google.com/", "https://www.youtube.com/"]
    extracted_urls = extract_url(txt)

    assert urls_from_txt == extracted_urls
