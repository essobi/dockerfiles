FROM python:3.6-alpine
MAINTAINER Shiqiao Du <lucidfrontier.45@gmail.com>

RUN set -x \
    && apk update \
    && apk add --virtual .build-deps \
        bzip2-dev \
        gcc \
        libc-dev \
        linux-headers \
        make \
        openssl-dev \
        pcre-dev \
        zlib-dev \
    && pip install uwsgi --no-cache-dir \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" \
    && apk add --virtual .uwsgi-rundeps $runDeps \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/*

COPY mime.types /etc/mime.types
