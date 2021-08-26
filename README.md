# Automatically Update Open PRs
This Github Action will automatically update your PRs whenever the main branch
has new commits. If you also enable Github's
[automerge](https://docs.github.com/en/github/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request)
feature then your PR will automatically be merged once it passes all checks like
CI or PR review.

## Usage
Add the following Github Action to your repository, for instance in
`.github/workflows/pr-auto-merge.yml`:

  ```yaml
  name: Merge base branch into PRs

  on:
    push:
      branches:
      # Automatically merge main/master branch into PR local branch.
        - main

  jobs:
    merge:
      name: PR base merge
      runs-on: ubuntu-latest
      strategy:
        max-parallel: 1
      steps:
      - name: PR base merge
        uses: deliveryhero/pr-base-auto-merger@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          # Delay in seconds between consecutive merges
          MERGE_DELAY: 5
          # Label of PRs for which base can be merged. Use '*' to include all open PRs.
          MERGE_LABEL: 'auto-base-merge'

  ```

## How It Works
The GH Action will trigger whenever there are new commits on the main/master
branch. It will then scan all PRs and automatically update those that have the
`MERGE_LABEL` (see Github Action snippet above) on them.

## TO-DO
- Add option to automerge base branch for only approved PRs to reduce unnecessary master merges
