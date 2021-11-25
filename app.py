
# Get user input
query = input("Isearch qquery requeried: ")

# As long as the query is valid (not empty or equal to '#')...

if query != '':
    noOfTweet = input("Enter the number of tweets you want to Analyze: ")
    if noOfTweet != '':
        noOfDays = input("Enter the number of days you want to Scrape Twitter for: [1 for today]: ")

        if noOfDays != '':
            # Creating list to append tweet data
            tweets_list = []
            now = datetime.date.today()

            now = now.strftime('%Y-%m-%d')

            yesterday = datetime.date.today() - datetime.timedelta(days=int(noOfDays))
            # it is extremely recommended to use UTC time stamp, to have a one global time reference! you computer date
            # is NOT UTC
            yesterday = yesterday.strftime('%Y-%m-%d')
            # scraper = twitterScraper.TwitterUserScraper(query, False)
            print("Please wait, scraping tweeter ...")
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:en since:' + yesterday + ' until:'
                                                                     + now + ' -filter:links -filter:replies')
                                              .get_items()):
                if i > int(noOfTweet):
                    break

                tweet.content = CT(tweet.content)  # why it is not working!?
                tweets_list.append({"id": tweet.id, "content": tweet.content, "Date": tweet.date})

            filename = 'tweets_lebanon' + datetime.datetime.now().strftime("_%Y_%m_%d") + '.json'
            f = open(filename, "w")
            # to overcome serialization of datetime use the default transfer to str for all
            j = json.dumps(tweets_list, indent=4, sort_keys=True, default=str)
            f.write(j)
            f.close()

            print(f"\nJson File {filename} Is Successfully Created!")
# learn more about "access modifier", private public, inheritance, polymorphism,
# you can create a Batch file to run a scheduled file, using Microsoft task scheduler
