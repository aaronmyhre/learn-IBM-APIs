import json, sys, os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='91e92695-0071-4f21-a3db-796e58820ec6',
    password='2iekqj0OvEWZ',
    version='2016-05-19')

homeDir = dirname(sys.path[0])

with open(os.path.join(homeDir, 'realdonaldtrump-tweets.json')) as trump_tweet_json:
    #content = json.load(trump_tweet_json)
    #textList = [x["text"] for x in content]
    #text = " ".join(textList)
    #print(type(text))
    text = json.load(trump_tweet_json)[0]['text']

    tone = tone_analyzer.tone(text, tones=None, sentences=None, content_type='text/plain')

    print(json.dumps(tone, indent=2))
