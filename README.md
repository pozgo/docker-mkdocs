### MkDocs in a docker.

[![Build Status](https://travis-ci.org/pozgo/docker-mkdocs.svg)](https://travis-ci.org/pozgo/docker-mkdocs)  
[![GitHub Open Issues](https://img.shields.io/github/issues/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs/issues)
[![GitHub Stars](https://img.shields.io/github/stars/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs)
[![GitHub Forks](https://img.shields.io/github/forks/pozgo/docker-mkdocs.svg)](https://github.com/pozgo/docker-mkdocs)  
[![Stars on Docker Hub](https://img.shields.io/docker/stars/polinux/mkdocs.svg)](https://hub.docker.com/r/polinux/mkdocs)
[![Pulls on Docker Hub](https://img.shields.io/docker/pulls/polinux/mkdocs.svg)](https://hub.docker.com/r/polinux/mkdocs)  
[![](https://images.microbadger.com/badges/version/polinux/mkdocs.svg)](http://microbadger.com/images/polinux/mkdocs)
[![](https://images.microbadger.com/badges/license/polinux/mkdocs.svg)](http://microbadger.com/images/polinux/mkdocs)
[![](https://images.microbadger.com/badges/image/polinux/mkdocs.svg)](http://microbadger.com/images/polinux/mkdocs)

[Docker Image](https://registry.hub.docker.com/u/polinux/mkdocs/) with [MkDocs](http://www.mkdocs.org/). It's using tiny image provided by Alpine.  
MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

Purpose of this image was to simplify the process of deploying MkDocs. This image is based on Alpine Linux to minimize the size of the image.

Workdir is set to `/mkdocs`

### Usage

    docker run \
      -ti \
      --name mkdocs \
      polinux/mkdocs

Mount Volume into working directory and make it available on port `80` on `localhost`.

    docker run \
      -ti \
      --name mkdocs \
      -p 80:8000 \
      -v /my_docs_dir:/mkdocs \
      polinux/mkdocs

Docker Compose file contains default settings for deploying in local directory and it's set to bind port `8000` to localhost.


### Build

    docker build -t polinux/mkdocs .

Docker troubleshooting
======================

Use docker command to see if all required containers are up and running:
```
$ docker ps
```

Check logs of mkdocs server container:
```
$ docker logs mkdocs
```

Sometimes you might just want to review how things are deployed inside a running
 container, you can do this by executing a _bash shell_ through _docker's
 exec_ command:
```
docker exec -ti mkdocs /bin/bash
```

History of an image and size of layers:
```
docker history --no-trunc=true polinux/mkdocs | tr -s ' ' | tail -n+2 | awk -F " ago " '{print $2}'
```

## Author

Przemyslaw Ozgo (<linux@ozgo.info>)