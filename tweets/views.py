import csv
import twitter
from django.conf import settings

from django.shortcuts import render

from Maplecroft.settings import BASE_DIR


def tweets(request):
    tweets_list = []
    map_labels = []
    with open(BASE_DIR + '/tweets/countries.csv', 'r') as f:
        reader = csv.reader(f)
        countries = list(reader)

    api = twitter.Api(consumer_key=getattr(settings, 'TWITTER_CONSUMER_KEY'),
                      consumer_secret=getattr(settings, 'TWITTER_CONSUMER_SECRET'),
                      access_token_key=getattr(settings, 'TWITTER_OAUTH_TOKEN'),
                      access_token_secret=getattr(settings, 'TWITTER_OAUTH_SECRET'))

    statuses = api.GetUserTimeline(screen_name='maplecroftrisk', count=10)

    [tweets_list.append(s.text) for s in statuses]

    for index, tweet in enumerate(tweets_list):
        map_labels.append([65.405957, 33.857576, index])

    return render(request, 'index.html', {'tweets': tweets_list, 'labels': map_labels})
