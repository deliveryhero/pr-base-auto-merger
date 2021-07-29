# pr-base-auto-merger
Automatically merge branch from base(main/master) into all open PR local branches. So add auto-base-merge label + enable [automerge](https://docs.github.com/en/github/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) on github UI and your PR will be automatically merged after approval without any worry of out of sync PR local branch.

## How it works?
- GH action job will be triggered when there is push to main/master branch by merging PR or direct commit.
- GH action job will update open PRs by merging branch from base(main/master) into local branches.

Features:
- You can specify delay between merges by `MERGE_DELAY` env variable to avoid load on CI/CD tools,atlantis etc.
- You can specify lable of PRs for which base can be merged by `MERGE_LABEL` env variable.You can set it to `*` to include all open PRs ignoring labels.


## Steps to onboard repo
- Just add below to github actions workflow yaml in `.github/workflows/` folder
  ```
  name: Merge base branch into PRs

  on:
    push:
      branches:
      # Automatically merge branch from base(main/master) into PR local branch
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
          # Lable of PRs for which base can be merged.Set it to '*' to include all open PRs
          MERGE_LABEL: 'auto-base-merge'

  ```

## TO-DO features
- Add option to automerge base branch for only approved PRs to reduce unnecessary master merges
