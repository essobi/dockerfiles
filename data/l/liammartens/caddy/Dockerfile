# @arg Override the alpine non-root user  
ARG USER=www-data  
  
# @from Builder  
FROM abiosoft/caddy:builder AS builder  
  
# @arg Build options  
ARG VERSION="0.10.11"  
ARG
PLUGINS="cache,cgi,cors,expires,ipfilter,minify,nobots,proxyprotocol,ratelimit"  
# @run Build it  
RUN VERSION=${VERSION} PLUGINS=${PLUGINS} /bin/sh /usr/bin/builder.sh  
  
# @from Actual image  
FROM liammartens/alpine  
LABEL maintainer="Liam Martens <hi@liammartens.com>"  
  
# @arg ping port  
ARG PING_PORT  
  
# @env default caddy path  
ENV CADDYPATH=/etc/certificates  
  
# @env ping port  
ENV PING_PORT=${PING_PORT:-65535}  
  
# @user Set user to root for installation  
USER root  
  
# @run add necessary packages  
RUN apk add tar libcap  
  
# @run mkdirs  
RUN mkdir -p /etc/certificates /var/www  
  
# @copy Copy default caddyfile  
COPY .docker ${DOCKER_DIR}/  
  
# @run own it  
RUN own  
  
# @run chown the dirs  
RUN chown -R ${USER}:${USER} /etc/certificates /var/www  
  
# @run chmod the dirs  
RUN chmod -R 750 /var/www  
  
# @run chmod the certificates directory  
RUN chmod -R 700 /etc/certificates  
  
# @copy Add caddy binary  
COPY \--from=builder /install/caddy /usr/bin/caddy  
  
# @run allow caddy to bind to ports without root  
RUN setcap 'cap_net_bind_service=+ep' $(which caddy)  
  
# @user Set user back to non-root  
USER ${USER}  
  
# @healthcheck Define healthcheck  
HEALTHCHECK \--interval=30s --timeout=30s --start-period=5s --retries=2 CMD
curl localhost:${PING_PORT} || exit 1

