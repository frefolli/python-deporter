# Deporter

CLI Utility for moving and handling multiple Git Server origins

# .config

## Source File

In Yaml format:

| key | value |
| --- | --- |
| `<USER>_USERNAME` | `USER` username |
| `<USER>_TOKEN` | `USER` token |
| `{NAME}_GITEA_URL` | Gitea `NAME` instance url |

# Installation

## Arch Linux

Download PKGBUILD from Releases and `makepkg -si` it.

## Manual Packaging

Executing `make package` will build a package instead of a python wheel, therefore you should be able to install the pip package inside `dist/`.
