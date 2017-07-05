import json, sys, os
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

"""
The example returns a JSON response whose content is the same as that in
   ../resources/personality-v3-expect2.txt
"""

homeDir = dirname(sys.path[0])

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='8cb2efe2-37d9-465f-83c9-e758c682a141',
    password='UAlr4bveGRLp')

with open(os.path.join(homeDir, 'jerry_holkins.txt'), 'r') as text:
    print(text)
    profile = personality_insights.profile(
            text,
            content_type='text/plain;charset=UTF8',
            raw_scores=False,
            consumption_preferences=False)

    print(json.dumps(profile, indent=2))
