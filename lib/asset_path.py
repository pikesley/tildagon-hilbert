# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps//"

if "github_user_tildagon_hilbert" in apps:
    ASSET_PATH = "/apps/github_user_tildagon_hilbert/"

if "hilbert" in apps:
    ASSET_PATH = "apps/hilbert/"
