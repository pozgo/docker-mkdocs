FROM alpine:latest

ENV MKDOCS_VERSION=1.0.4 \
    DOCS_DIRECTORY='/mkdocs' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false' \
    FAST_MODE='false'

ADD bootstrap/ /bootstrap

RUN \
    apk add --update \
        ca-certificates \
        bash \
        git \
        openssh \
        python3 \
        python3-dev && \
    pip3 install --upgrade pip && \
    pip install mkdocs==${MKDOCS_VERSION} && \
    cd /bootstrap && pip install -e /bootstrap && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

WORKDIR ${DOCS_DIRECTORY}

CMD ["/usr/bin/bootstrap", "start"]
