from src.text_preprocessing.extract import extract_hashtags
from src.text_preprocessing.extract import extract_user_mentions

def test_extract_hashtag():
    txt =  "This text contains hashtags #be-happy and #test"
    hashtags_from_txt = ['#be-happy', '#test']
    extracted_hashtags = extract_hashtags(txt)
    
    assert extracted_hashtags == hashtags_from_txt
    
def test_extract_user_mentions():
    txt =  "This text contains @user, @second_user, and @user3  mentions"
    user_mentions_from_txt = ['@user', '@second_user', '@user3']
    extracted_user_mentions = extract_user_mentions(txt)

    assert extracted_user_mentions == user_mentions_from_txt
    