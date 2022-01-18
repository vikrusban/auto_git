import argparse
import git
from urllib.parse import urlparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Script to download and update git repositories written in Python 3.10')
parser.add_argument("-f", help="File with a list of repositories", required=True)
parser.add_argument("-d", help="Folder for storing repositories", required=True)
args = parser.parse_args()

f = args.f
d = args.d

with open(f) as file:
    array = [row.strip() for row in file]

for i in array:
    link_repo = urlparse(i)
    link_repo_path = link_repo.path[1:]
    dir_repo = link_repo_path[link_repo_path.find("/") + 1 : ]
    dir = Path(d, dir_repo)

    if dir.is_dir():
        print('git pull '+i)
        g = git.cmd.Git(d+'/'+dir_repo)
        g.pull()
    else:
        print('git clone '+i)
        git.Repo.clone_from(i, d+'/'+dir_repo)