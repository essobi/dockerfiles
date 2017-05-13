FROM python:2.7-alpine

# init system for container
ARG TINI_VERSION=0.10.0
RUN apk add --no-cache --virtual .fetch-deps \
        ca-certificates \
        openssl \
        gnupg \
\
    && wget https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static \
    && wget https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static.asc \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 0527A9B7 \
    && gpg --verify /tini-static.asc \
    && rm -rf /tini-static.asc /root/.gnupg/ \
    && chmod +x /tini-static \
    && mv /tini-static /usr/local/bin/tini \
\
    && apk del .fetch-deps

ENTRYPOINT ["tini", "--"]
