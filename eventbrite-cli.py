#!/usr/bin/env python
import os
import sys
import json
import requests

def main(query):
    if query == 'attendees':
        res = []
        uri = "https://www.eventbriteapi.com/v3/events/%s/attendees/?token=%s" % (os.environ['EVENT_ID'], os.environ['OAUTH_TOKEN'])
        data = json.loads(requests.get(uri).text)
        for attendee in data['attendees']:
            res.append(attendee)
        has_more_items = data['pagination']['has_more_items']
        if has_more_items == 'true':
            continuation = data['pagination']['continuation']
            while True:
                uri = "https://www.eventbriteapi.com/v3/events/%s/attendees/?token=%s&continuation=%s" % (os.environ['EVENT_ID'], os.environ['OAUTH_TOKEN'], continuation)
                data = json.loads(requests.get(uri).text)
                for attendee in data['attendees']:
                    res.append(attendee)
                has_more_items = data['pagination']['has_more_items']
                if has_more_items == 'false':
                    break
                else:
                    continuation = data['pagination']['continuation']
    res_all = ""
    for i in res:
        res_all+=str(i)
    return res_all

if __name__ == '__main__':
    print(main(sys.argv[1]))
