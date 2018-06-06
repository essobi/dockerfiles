FROM jenkins/jenkins:alpine  
MAINTAINER Francisco Berrocal <eu@chicocode.io>  
  
# Change to root user  
USER root  
  
# Docker and Docker Compose versions to be installed  
ARG DOCKER=17.06.2-ce  
ARG DOCKER_COMPOSE=1.16.1  
# Copy entrypoint  
COPY entrypoint.sh /  
  
# Copy semver tool  
COPY semver.sh /usr/local/bin/semver  
  
# Copy jenkins plugins  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
  
RUN set -x \  
&& apk update \  
  
# Install docker  
&& curl -fsSLO
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER:-17.06.2-ce}.tgz
\  
&& tar --strip-components=1 -xvzf docker-${DOCKER:-17.06.2-ce}.tgz -C
/usr/local/bin \  
  
# Install dos2unix shado jq (to fix file format from win systems)  
&& apk --no-cache add \--update --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ dos2unix shadow jq \  
  
# Install sudo (to run container as jenkins user)  
&& apk add sudo \  
  
# Fix jenkins plugins line endings  
&& dos2unix /usr/share/jenkins/ref/plugins.txt \  
  
# Install plugins  
&& /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt \  
  
# Fix entrypoint script line endings & turn entrypoint semver executable  
&& dos2unix /entrypoint.sh && apk del dos2unix \  
&& chmod a+rx /entrypoint.sh \  
&& chmod a+rx /usr/local/bin/semver \  
  
# Install docker compose  
&& apk add \--no-cache -t .deps ca-certificates curl \  
&& GLIBC_VERSION='2.23-r3' \  
&& curl -Lo /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& curl -Lo glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk \  
&& curl -Lo glibc-bin.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk \  
&& apk add glibc.apk glibc-bin.apk \  
&& rm -rf /var/cache/apk/* \  
&& rm glibc.apk glibc-bin.apk \  
&& apk del .deps \  
&& apk add --no-cache -t .deps ca-certificates curl \  
&& DOCKER_COMPOSE_URL=https://github.com$(curl -L
https://github.com/docker/compose/releases/latest | grep -Eo
'href="[^"]+docker-compose-Linux-x86_64' | sed 's/^href="//') \  
&& curl -Lo /usr/local/bin/docker-compose $DOCKER_COMPOSE_URL \  
&& chmod a+rx /usr/local/bin/docker-compose \  
&& apk del .deps  
  
# Set entrypoint  
ENTRYPOINT ["/bin/bash","-c","./entrypoint.sh"]  
  
# Allow directory browser for any script  
ENV JAVA_OPTS -Dhudson.model.DirectoryBrowserSupport.CSP=""  

