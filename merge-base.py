import argparse
import json
from github import Github

def main(args):
    with open(args.event_path) as event_file:
        event = json.load(event_file)
    g = Github(args.github_token)
    repo = g.get_repo(event['repository']['full_name'])
    print(repo.name)
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
      print(pr.number)
      repo.merge(pr.head.ref, pr.base.ref)

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--github_token", help="Token for GitHub API")
parser.add_argument("-e", "--event_path", help="JSON file path of GitHub event `POST` webhook payload")

args = parser.parse_args()

main(args)
