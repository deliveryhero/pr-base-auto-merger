FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install PyGithub

COPY merge-base.py merge-base.py

CMD python merge-base.py --github_token $GITHUB_TOKEN --event_path $GITHUB_EVENT_PATH --merge_delay $MERGE_DELAY --merge_label $MERGE_LABEL
