# pr-base-auto-merger
automatically merge branch from base(main/master) into PR local branch.

Just add below to github actions workflow yaml 
GH action job will be triggered when there is push to main/master branch by merging PR or direct commit.
```
name: Merge base branch into PRs


on:
  push:
    branches:
    # automatically merge branch from base(main) into PR local branch
      - main
    # automatically merge branch from base(master) into PR local branch
    #  - master

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
```
