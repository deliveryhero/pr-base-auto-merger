# pr-base-auto-merger
automatically merge branch from base(main/master) into all open PR local branches.


GH action job will be triggered when there is push to main/master branch by merging PR or direct commit.

Just add below to github actions workflow yaml
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
        # Delay between consecutive merges
        MERGE_DELAY: 5
```

## TO-DO features
- Add option to automerge base branch for only approved PRs to reduce unnecessary master merges
- Exclude PR with certain labels
