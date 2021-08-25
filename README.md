# pr-base-auto-merger
Automatically merge main/master branch into all open PRs. So add auto-base-merge label + [enable automerge](https://docs.github.com/en/github/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) on Github UI and your PR will be automatically merged after approval without any worry of out of sync PR local branch.

## How it works?
- GH action job will be triggered when there is a push to main/master branch by merging PR or direct commit.
- GH action job will update open PRs and merge the main/master branch into the local branches.

Features:
- You can specify a delay between merges via the `MERGE_DELAY` env variable to avoid load on CI/CD tools, Atlantis etc.
- You can specify label of PRs for which base can be merged by `MERGE_LABEL` env variable.You can set it to `*` to include all open PRs ignoring labels.


## Steps to onboard repo
- Just add below to Github Actions workflow YAML in the `.github/workflows/` folder:
  ```
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

## TO-DO features
- Add option to automerge base branch for only approved PRs to reduce unnecessary master merges
