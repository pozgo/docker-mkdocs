### MkDocs in a docker.

[![Docker Image MKDocs](https://github.com/pozgo/docker-mkdocs/workflows/Docker%20Image%20MKDocs/badge.svg?branch=master)](https://github.com/pozgo/docker-mkdocs/actions?query=workflow%3A%22Build+%26+Test+MKDocs%22)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fpozgo%2Fdocker-mkdocs.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fpozgo%2Fdocker-mkdocs?ref=badge_shield)

[![GitHub Open Issues](https://img.shields.io/github/issues/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs/issues)
[![GitHub Stars](https://img.shields.io/github/stars/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs)
[![GitHub Forks](https://img.shields.io/github/forks/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs)  
[![](https://img.shields.io/github/release/pozgo/docker-mkdocs.svg)](http://microbadger.com/images/pozgo/docker-mkdocs)
[![](https://images.microbadger.com/badges/image/polinux/mkdocs.svg)](http://microbadger.com/images/polinux/mkdocs)

[![Docker build](http://dockeri.co/image/polinux/mkdocs)](https://hub.docker.com/r/polinux/mkdocs/)

Felling like supporting me in my projects use donate button. Thank You!  
[![](https://img.shields.io/badge/donate-PayPal-blue.svg)](https://www.paypal.me/POzgo)

[Docker Image](https://registry.hub.docker.com/u/polinux/mkdocs/) with [MkDocs](http://www.mkdocs.org/). It's using tiny image provided by Alpine.  
MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

Purpose of this image was to simplify the process of deploying MkDocs. This image is based on Alpine Linux to minimize the size of the image.

```yaml
version: '3'

services:
  mkdocs:
    container_name: mkdocs
    image: polinux/mkdocs:1.1.2
    restart: always
    ports:
      - "8000:8000"
    environment:
      LIVE_RELOAD_SUPPORT: 'true'
      ADD_MODULES: 'fontawesome-markdown mkdocs-git-revision-date-localized-plugin mkdocs-material'
      FAST_MODE: 'true'
      DOCS_DIRECTORY: '/mkdocs'
      GIT_REPO: 'git@github.com:username/docs.git'
      UPDATE_INTERVAL: 15
      AUTO_UPDATE: 'true'
    volumes:
      - $HOME/.ssh/id_rsa:/root/.ssh/id_rsa
```

### Environmental Variables

|Variable|Notes|Default|
|:--|:--|---|
|`LIVE_RELOAD_SUPPORT`|Support for live reload feature. |`false`|
|`ADD_MODULES`|List of module to install.|`false`|
|`FAST_MODE`|Enable fast mode. Rebuilds only changed/added files|`false`|
|`DOCS_DIRECTORY`|Directory in which documentation is mounted inside of container|`/mkdocs`|
|`GIT_REPO`|Repository address. Will require ssh key for ssh connection. Example: `-v ${HOME}/.ssh/id_rsa:/root/.ssh/id_rsa`|`false`|
|`GIT_BRANCH`|Self explanatory|`master`|
|`AUTO_UPDATE`|Auto update for git repository support|`false`|
|`UPDATE_INTERVAL`|Update interval in *minutes* - used only when `AUTO_UPDATE` set to `true`|every `15` minutes|
|`DEV_ADDR`|Custom IP address and port to serve documentation locall|`0.0.0.0:8000`|

### Usage

```bash
docker run \
    -ti \
    --name mkdocs \
    polinux/mkdocs
```

Custom config with `git` repository as source of documentation
```bash
docker run \
    -ti \
    --name mkdocs \
    -p 80:9000 \
    -e "ADD_MODULES=mkdocs-bootstrap mkdocs-gitbook mkdocs-bootstrap4" \
    -e "LIVE_RELOAD_SUPPORT=true" \
    -e "FAST_MODE=true" \
    -e "DOCS_DIRECTORY=/my_docs" \
    -e "GIT_REPO=https://my_repos/custom-docs.git" \
    -e "GIT_BRANCH=develop" \
    -e "AUTO_UPDATE=true" \
    -e "UPDATE_INTERVAL=1" \
    -e "DEV_ADDR=0.0.0.0:9000" \
    -v ${HOME}/.ssh/id_rsa:/root/.ssh/id_rsa \
    polinux/mkdocs
```

See `docker-compose.yaml` for all compose options examples

### Update git repo based deployment
Assuming you are using git repository as source of documentation there are two options available for updating the content of the docs.

#### Manual

Assuming that container name is `mkdocs`  
```bash
docker exec -ti mkdocs bootstrap update
Pulled branch: master
Commit: a4000c525f6db977777bf758987c4df0b44f59b4
Commit Message: Updated nodejs
Date: 2020-03-24 18:52:43
Author: Przemek Ozgo
```

#### AUTO_UPDATE
there are two environmental variables that can be used for AUTO UPDATE.
See table above ^^


### Build

```bash
docker build -t polinux/mkdocs .
```

Docker troubleshooting
======================

Use docker command to see if all required containers are up and running:

```bash
docker ps
```

Check logs of mkdocs server container:

```bash
docker logs mkdocs
```

Sometimes you might just want to review how things are deployed inside a running
 container, you can do this by executing a _bash shell_ through _docker's
 exec_ command:

```bash
docker exec -ti mkdocs /bin/bash
```

History of an image and size of layers:

```bash
docker history --no-trunc=true polinux/mkdocs | tr -s ' ' | tail -n+2 | awk -F " ago " '{print $2}'
```

## Author

Przemyslaw Ozgo

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fpozgo%2Fdocker-mkdocs.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fpozgo%2Fdocker-mkdocs?ref=badge_large)