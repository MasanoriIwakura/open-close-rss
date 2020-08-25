import feedparser
import urllib.parse


RSS_URL = 'https://kaiten-heiten.com/category/sightseeing-leisure/{0}/feed/'

CATEGORIES = {
    'capsule': 'capsule',
    'hotel': 'hotel-businesshotel',
    'resort': 'resort',
    'ryokan': 'ryokan'
}

STATUS = {
    'open': '【開店】',
    'close': '【閉店】'
}


def get_query(status):
    return f'?s={urllib.parse.quote(status)}'


def read_close_rss(category):
    feed = feedparser.parse(RSS_URL.format(
        category) + get_query(STATUS['close']))
    for entry in feed.entries:
        updated = entry.updated_parsed
        print(entry.title, entry.link, f'{updated.tm_year}/{updated.tm_mon}/{updated.tm_mday}')


if __name__ == "__main__":
    for category in CATEGORIES.values():
        read_close_rss(category)
