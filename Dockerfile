FROM alpine:latest

ENV MKDOCS_VERSION=1.1.0 \
    DOCS_DIRECTORY='/mkdocs' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false' \
    FAST_MODE='false' \
    PYTHONUNBUFFERED=1 \
    GIT_REPO='false' \
    GIT_BRANCH='master' \
    AUTO_UPDATE='false' \
    UPDATE_INTERVAL=15

ADD container-files/ /

RUN \
    apk add --update \
        ca-certificates \
        bash \
        git \
        openssh \
        python3 \
        python3-dev \
        build-base && \
    pip3 install --upgrade pip && \
    pip install mkdocs==${MKDOCS_VERSION} && \
    cd /bootstrap && pip install -e /bootstrap && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* && \
    chmod 600 /root/.ssh/config

CMD ["/usr/bin/bootstrap", "start"]
