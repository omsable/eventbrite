#!/usr/bin/env python

import os
import sys
import json
import requests


def main(query, *args):
    if query == 'attendees':
        event_id = args[0] if args else os.environ['EVENT_ID']
        url = (
            'https://www.eventbriteapi.com'
            '/v3/events/{}/attendees'
            '?token={}&continuation=%s'
        ).format(event_id, os.environ['OAUTH_TOKEN'])

        attendees = []
        continuation = ''
        while True:
            res = requests.get(
                url % continuation
            )

            try:
                res.raise_for_status()
            except:
                sys.stderr.write(res.text)
                raise
            else:
                data = res.json()

                attendees.extend(data['attendees'])

                has_more_items = data['pagination']['has_more_items']
                if has_more_items:
                    continuation = data['pagination']['continuation']
                else:
                    break

        return attendees


if __name__ == '__main__':
    sys.stdout.write(json.dumps(main(*sys.argv[1:])))
