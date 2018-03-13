FROM          alpine:3.7

ADD           install.sh /install.sh
ADD           entrypoint.sh /entrypoint.sh
ADD           eventbrite-cli.py /eventbrite-cli.py
RUN           /install.sh && rm -f /install.sh

ENTRYPOINT   ["/entrypoint.sh"]
