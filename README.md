# pr-base-auto-merger
Automatically merge branch from base(main/master) into all open PR local branches.

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
        uses: docker://suyogpatil36/pr-base-auto-merger:1.0.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          # Delay in seconds between consecutive merges
          MERGE_DELAY: 5
          # Lable of PRs for which base can be merged.Set it to '*' to include all open PRs
          MERGE_LABEL: 'auto-base-merge'

  ```

## TO-DO features
- Add option to automerge base branch for only approved PRs to reduce unnecessary master merges
