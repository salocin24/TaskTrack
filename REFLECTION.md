# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?
- The local TaskTrack repository does not instantly upload or pull changes from the repository hosted on GitHub until explicitly told to do so. The local repository can run without an internet connection.

## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?
- Just because we are connected to a GitHub repository does not mean that we are pushing to a GitHub repository. That would defeat the whole purpose of Git if it would automatically replace our own files once connected.

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?
- Cloning a repository keeps the commit history viewable. A .zip would only contain the project files, not the hidden Git files that are included in a repo.

## 4. Fetching and Pulling

What information did `git fetch` update, and what additional action did `git pull` perform?
- git fetch responds with the differences between your local git repo, and the up to date GitHub repo. It will respond with ahead/behind depending on your status in comparison with the remote GitHub repository. Git pull is run after git fetch, pulling the changes made in the GitHub repository to your local Git repository, updating your project files to match those that are hosted remotely.

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?
- So it is easier for us and others to look through at a later date. One big commit is more cumbersome to parse, so many small ones with explicit commit messages is best practice.