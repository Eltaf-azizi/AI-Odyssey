import GetOldTweets3 as got
import string
from typing import Counter
import matplotlib.pyplot as plt


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \ 
        .setSince("2019-05-01") \ 
        .setUntil("2020-09-30") \
        .setMaxTweets(10)
    
    #List of object gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Iterating through tweets list. Storing them temp in tweet variable.
    # Get text and store it as a list inside text_tweets
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text


# Reading text file
# text = open('text.txt', encoding='utf-8').read()


# Converting to lowerCase
lower_case = text.lower()


# Removing punctuation
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))


#spliting text file words
tokenized_word = cleaned_text.split()



stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


final_words = []
for word in tokenized_word:
    if word not in stop_words:
        final_words.append(word)


# NLP emotion algorithm
# 1) check if the word in the final word list is also present in emotion.txt
# - open the emotion file
# - loop through each line and clear it
# - extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list


emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)


print(emotion_list)
w = Counter(emotion_list)
print(w)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()