# pr-base-auto-merger
automatically merge branch from base(master) into PR local branch

Just add below to github actions workflow yaml and everything should start working
```
name: Merge base branch into PRs

on:
  push:
    branches:
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
```
