tweet=input('your tweet: \n')

split_tweet=tweet.split()

num_words=len(split_tweet)
num_chars=len(tweet)
print("*********************************************")
if num_chars > 280:
    print(f"you have use {num_chars-280} more charecters than allowed! ")
else:
    print(f"you have use {num_chars-280} charectors remaining")
print("*********************************************")
print(f"number of words: {num_words}")
print(f"number of charactors: {num_chars}")
print("*********************************************")


print(f"your tweet: \n{tweet[:280]}")