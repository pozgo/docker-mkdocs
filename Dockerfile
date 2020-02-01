FROM alpine:latest

ENV MKDOCS_VERSION=1.0.4 \
    GIT_REPO='false' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false'

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
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

COPY container-files /

RUN chmod +x /bootstrap.sh

WORKDIR /workdir

ENTRYPOINT ["/bootstrap.sh"]
