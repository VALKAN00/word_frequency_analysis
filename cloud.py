import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


nltk.download('stopwords')
nltk.download('punkt')


with open("paragraphs.txt", "r") as file:
    text = file.read()



words = nltk.word_tokenize(text)


stopwords_list = set(stopwords.words('english'))


filtered_words = [word for word in words if word.lower() not in stopwords_list]


word_counts = Counter(filtered_words)


for word, count in word_counts.most_common():
    print(f"{word}: {count}")
