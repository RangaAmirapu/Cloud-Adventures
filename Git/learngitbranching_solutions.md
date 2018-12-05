


> Written with [StackEdit](https://stackedit.io/).

# Introduction Sequence

### Introduction to Git Commits

    git commit
    git commit

### Branching in Git

    git checkout -b bugFix

### Merging in Git

    git checkout -b bugFix
    git commit
    git checkout master
    git commit
    git merge bugFix
    
### Rebase Introduction

    git checkout -b bugFix
    git commit
    git checkout master
    git commit
    git checkout bugFix
    git rebase master

### Detach yo' HEAD

    git checkout -b bugFix

### Relative Refs (^)

    git checkout bugFix^
    
### Relative Refs (~)

    git branch -f bugFix c0
	git branch -f master c6
	git checkout c1

### Reversing Changes in Git

	git reset local~1
	git checkout pushed
	git revert pushed

# Moving Work Around

### Cherry-pick Intro
	git cherry-pick c3 c4 c7

### Interactive Rebase Intro
		git rebase -i master~4

# A Mixed Bag

### Grabbing Just 1 Commit

	git checkout master
	git cherry-pick c4

###  Juggling Commits

	git rebase -i caption~2
	git commit --amend
	git rebase -i caption~2
	git branch -f master c3''

###  Juggling Commits #2
	git checkout master
	git cherry-pick c2
	git checkout c1
	git cherry-pick c2' c3
	git branch -f master c3'
	
###  Git Tags

    git checkout c2
    git tag v1 c2
    git tag v0 c1


###  Git Describe

    git describe c6
    git commit

