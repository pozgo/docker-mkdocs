FROM alpine:latest

ENV MKDOCS_VERSIO="0.16.3"

RUN \
    apk add --update \
        ca-certificates \
        bash \
        python2 \
        python2-dev \
        py-setuptools && \
    easy_install-2.7 pip && \
    pip install mkdocs==${MKDOCS_VERSIO} && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

COPY container-files /

ENTRYPOINT ["/bootstrap.sh"]