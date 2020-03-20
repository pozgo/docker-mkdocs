FROM alpine:latest

ENV MKDOCS_VERSION=1.1 \
    DOCS_DIRECTORY='/mkdocs' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false' \
    FAST_MODE='false' \
    PYTHONUNBUFFERED=1

ADD bootstrap/ /bootstrap

RUN \
    apk add --update \
        ca-certificates \
        bash \
        git \
        openssh \
        make \
        python2 \
        python3 \
        python3-dev && \
    pip3 install --upgrade pip && \
    pip install mkdocs==${MKDOCS_VERSION} && \
    cd /bootstrap && pip install -e /bootstrap && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*
    pip install pygments mkdocs-material pymdown-extensions mkdocs-awesome-pages-plugin   

WORKDIR ${DOCS_DIRECTORY}

CMD ["/usr/bin/bootstrap", "start"]
