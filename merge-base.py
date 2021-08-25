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
    parser.add_argument("-d", "--merge_delay", help="Delay between merges")
    parser.add_argument("-l", "--merge_label",
                        help="Automatically update PRs with this label")
    parser.add_argument("-g", "--github_token", help="GitHub API token")
    parser.add_argument("-e", "--event_path",
                        help="Path to GitHub's POST webhook payload")

    main(parser.parse_args())
