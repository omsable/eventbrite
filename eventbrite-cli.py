#!/usr/bin/env python
import os
import sys
from eventbrite import Eventbrite

def main(arg):
    if arg == 'attendees':
        eventbrite = Eventbrite(os.environ['OAUTH_TOKEN'])
        attendees = eventbrite.get_event_attendees(os.environ['EVENT_ID'])
        return attendees

if __name__ == '__main__':
    print(main(sys.argv[1]))
