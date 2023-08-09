from src.text_preprocessing.extract import extract_hashtags

def test_extract_hashtag():
    txt =  "This text contains hashtags #be-happy and #test"
    hashtags_from_txt = ['#be-happy', '#test']
    extracted_hashtags = extract_hashtags(txt)
    
    assert extracted_hashtags == hashtags_from_txt
    