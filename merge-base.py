import argparse
import json
import time

from github import Github


def main(args):
    with open(args.event_path) as event_file:
        event = json.load(event_file)
    g = Github(args.github_token)
    repo = g.get_repo(event['repository']['full_name'])
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
        found = 0
        for label in pr.get_labels():
            if label.name == args.merge_label:
                found = 1
                break
        if args.merge_label == "*" or found == 1:
            try:
                repo.merge(pr.head.ref, pr.base.ref)
                print(f"Merged base branch to PR #{pr.number}")
                time.sleep(int(args.merge_delay))
            except:
                print(
                    f"Merge of base branch failed for PR #{pr.number}! "
                    "Please check for merge conflicts."
                )


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--merge_delay", help="Delay between merges")
parser.add_argument("-l", "--merge_label",
                    help="Label of PRs for which base can be merged")
parser.add_argument("-g", "--github_token", help="Token for GitHub API")
parser.add_argument("-e", "--event_path",
                    help="JSON file path of GitHub event `POST` webhook payload")

args = parser.parse_args()

main(args)
