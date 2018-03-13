#!/usr/bin/env python
import os
from eventbrite import Eventbrite

eventbrite = Eventbrite(os.environ['OAUTH_TOKEN'])
attendees = eventbrite.get_event_attendees(os.environ['EVENT_ID'])
print(attendees)
