FROM python:3.8-alpine

RUN apk --no-cache add bash
RUN pip install --upgrade pip
RUN pip install PyGithub

ADD entrypoint.sh /entrypoint.sh
COPY merge-base.py /app/merge-base.py
ENTRYPOINT ["/entrypoint.sh"]
