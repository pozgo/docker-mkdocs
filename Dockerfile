FROM alpine:latest

ENV MKDOCS_VERSION="0.17.2"

RUN \
    apk add --update \
        ca-certificates \
        bash \
        python2 \
        python2-dev \
        py-setuptools && \
    easy_install-2.7 pip && \
    pip install mkdocs==${MKDOCS_VERSION} && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

COPY container-files /

ENTRYPOINT ["/bootstrap.sh"]