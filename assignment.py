import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')


with open('random_paragraphs.txt', 'r') as file:
    content = file.read()
    

words = nltk.word_tokenize(content)

stop_words = set(stopwords.words('english'))

def remove_stop_words(sentence): 
    words = sentence.split() 
    
    filtered_words = [word for word in words if word not in stop_words] 
    
    return ' '.join(filtered_words)

filtered_content=remove_stop_words(content)
word_freq = Counter(filtered_content)
for word, freq in word_freq.items():
    print(f"The word '{word}' appears {freq} times.")

count_stop_words_original = sum(1 for word in content.split() if word.lower() in stop_words)
count_Of_Words_of_article= len(content.split())
count_Of_Words_of_filtered=len(filtered_content.split())


print("Count of Words in original article :",f"{count_Of_Words_of_article:,}")
print("Count of Stop Words in original article:", f"{count_stop_words_original:,}")
print("Count of Words in filtered article :",f"{count_Of_Words_of_filtered:,}")


    
   