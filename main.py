#!/usr/bin/env python
import lib.commons.Gitea as Gitea
import lib.commons.Github as Github
import lib.commons.Credentials as Credentials
import lib.commons.User as User

gitea = Gitea.from_env("REFOLINUX")
github = Github()

github_creds = Credentials.from_env("FREFOLLI_GITHUB")
gitea_creds = Credentials.from_env("FREFOLLI_GITEA")

github_user = User("frefolli")
gitea_user = User("frefolli")

def identify_repositories(platform, user, credentials):
    for repo in platform.get_user_repositores(user, credentials):
        print("In[%s]::Found[%s]" % (str(platform), str(repo)))

identify_repositories(github, github_user, github_creds)
identify_repositories(gitea, gitea_user, gitea_creds)
