FROM          jfloff/alpine-python

ADD           app.py /app.py
RUN           pip install eventbrite

ENTRYPOINT   ["python", "/app.py"]
