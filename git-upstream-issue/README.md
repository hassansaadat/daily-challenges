# Prevent git keep asking to set upstream when you run `git push`

Command:
```bash
git push

fatal: The current branch fix/image-options-value has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin fix/image-options-value
```

## Answer
```bash
git config --global --add push.default current
git config --global --add push.autoSetupRemote true
```

Reference: https://stackoverflow.com/a/78085390/9811757
