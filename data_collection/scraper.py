import datetime
import json
from data_collection import twitter as tw


def search(query,size=-1):
    # Get user input

    tweets_list = []

    now = datetime.date.today()

    now = now.strftime('%Y-%m-%d')

    yesterday = datetime.date.today() - datetime.timedelta(days=int(1))

    yesterday = yesterday.strftime('%Y-%m-%d')
    print("Please wait, scraping tweeter ...")

    q = query + ' lang:en since:' + yesterday + ' until:' + now + ' -filter:links -filter:replies'

    for i, tweet in enumerate(tw.TwitterSearchScraper(q).get_items()):
        if i > -1:
            break

        tweets_list.append({"id": tweet.id,
                            "content": tweet.content,
                            "Date": tweet.date,
                            "Location": tweet.place,
                            "reply count": tweet.replyCount,
                            "retweet count": tweet.retweetCount,
                            "Like Count": tweet.likeCount,
                            "quoteCount": tweet.quoteCount,
                            })

    return tweets_list


# search('lebanon')


def save_tweets(tweets_list):
    filename = 'tweets_lebanon' + datetime.datetime.now().strftime("_%Y_%m_%d") + '.json'
    f = open(filename, "w")
    j = json.dumps(tweets_list, indent=4, sort_keys=True, default=str)
    f.write(j)
    f.close()
    print(f"\nJson File {filename} Is Successfully Created!")
