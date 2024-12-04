# text-preprocessing

A Python package performs a small collection of functions for preprocessing text. It contains the following functions tha transform a given text:

* Extracts:
  * Hashtags
  * User mentions
  * URL's
* Removes:
  * Hashtags
  * User mentions
  * URL's

## How to install the package

To install this package, run the following command:

```
 pip install pip@git+https://github.com/lilianabs/text_preprocessing
```

## How to use this package
Before using this package, make sure you have installed it.

To extract hashtags, user mentions, and URL's:

```
from text_preprocessing.extract import extract_hashtags
from text_preprocessing.extract import extract_user_mentions
from text_preprocessing.extract import extract_url

txt = "This text contains hashtags #be-happy and #test"
extracted_hashtags = extract_hashtags(txt)

txt = "This text contains @user, @second_user, and @user3  mentions"
extracted_user_mentions = extract_user_mentions(txt)

txt = """This text contains url https://www.google.com/ 
          and https://www.youtube.com/"""
extracted_urls = extract_url(txt)
```

To remove hashtags, user mentions, and URL's:

```
from text_preprocessing.remove import remove_hashtags
from text_preprocessing.remove import remove_user_mentions
from text_preprocessing.remove import remove_url

txt = "This text contains hashtags #be-happy and #test"
txt_removed_hashtags = remove_hashtags(txt)

txt = "This text contains @user, @second_user, and @user3  mentions"
txt_removed_user_mentions = remove_user_mentions(txt)

txt = """This text contains url https://www.google.com/ 
          and https://www.youtube.com/"""
txt_removed_urls = remove_url(txt)
```
