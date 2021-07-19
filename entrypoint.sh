#!/bin/bash
python /app/merge-base.py --github_token $GITHUB_TOKEN --event_path $GITHUB_EVENT_PATH --merge_delay $MERGE_DELAY --merge_label $MERGE_LABEL
