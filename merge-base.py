import argparse
import json
import time

from github import Github


def main(args):
    g = Github(args.github_token)

    # Fetch all PRs against the current repository.
    event = json.load(open(args.event_path))
    repo = g.get_repo(event['repository']['full_name'])
    pulls = repo.get_pulls(state='open', sort='created')

    # Merge the main/master branch if the PR was tagged with the correct label
    # (cf. `--merge_label` option).
    for pr in pulls:
        labels = {_.name for _ in pr.get_labels()}
        if args.merge_label == "*" or args.merge_label in labels:
            try:
                repo.merge(pr.head.ref, pr.base.ref)
                print(f"Merged base branch to PR #{pr.number}")
                time.sleep(int(args.merge_delay))
            except:
                print(
                    f"Merge of base branch failed for PR #{pr.number}! "
                    "Please check for merge conflicts."
                )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    padd = parser.add_argument
    padd("-d", "--merge_delay", help="Delay between merges")
    padd("-l", "--merge_label", help="Update all PRs with this label")
    padd("-g", "--github_token", help="GitHub API token")
    padd("-e", "--event_path", help="Path to GitHub's POST webhook payload")

    main(parser.parse_args())
