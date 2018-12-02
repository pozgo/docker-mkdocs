### MkDocs in a docker.

[![Build Status](https://travis-ci.org/pozgo/docker-mkdocs.svg?branch=master)](https://travis-ci.org/pozgo/docker-mkdocs)  
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

Workdir is set to `/workdir`

### Environmental Variables

|Variable|Notes|
|:--|:--|
|`GIT_REPO`|Remote git based repository - requires mounted keys *see examples below*|
|`LIVE_RELOAD_SUPPORT`|Support for live reload feature. Default set to `false` - Use if auto reload needed|

### Usage

```bash
docker run \
    -ti \
    --name mkdocs \
    polinux/mkdocs
```
Mount Volume into working directory and make it available on port `80` on `localhost`.

```bash
docker run \
    -ti \
    --name mkdocs \
    -p 80:8000 \
    -v /my_docs_dir:/workdir \
    polinux/mkdocs
```

Fetch from git repository with ssh keys shared from host os

```bash
docker run \
    -ti \
    --name mkdocs \
    -e GIT_REPO='git@github.com:username/my-repo.git' \
    -e LIVE_RELOAD_SUPPORT='true' \
    -v ~/.ssh:/root/.ssh:ro \
    polinux/mkdocs
```

`-v ~/.ssh:/root/.ssh:ro` - Mouts ssh keys from host OS and sets `read-only` permissions

Docker Compose file contains default settings for deploying in local directory and it's set to bind port `8000` to localhost.

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