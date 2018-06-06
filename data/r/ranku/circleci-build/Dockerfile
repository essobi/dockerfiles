FROM node:8.11.2-alpine  
  
# Install CircleCI Dependencies  
# See: https://circleci.com/docs/2.0/custom-images/#adding-required-and-
custom-tools-or-files  
RUN apk --update add git openssh openssl tar gzip && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
# Install glibc on Alpine (required by docker-compose) from  
# https://github.com/sgerrand/alpine-pkg-glibc  
# See also https://github.com/gliderlabs/docker-alpine/issues/11  
RUN set -x && \  
apk add --no-cache -t .deps ca-certificates curl && \  
GLIBC_VERSION='2.23-r3' && \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
curl -Lo glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk && \  
curl -Lo glibc-bin.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk && \  
apk update && \  
apk add glibc.apk glibc-bin.apk && \  
rm -rf /var/cache/apk/* && \  
rm glibc.apk glibc-bin.apk && \  
apk del .deps  
  
# Install Docker  
RUN set -ex \  
&& apk add --no-cache -t .deps ca-certificates curl \  
&& export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) \  
&&
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
\  
&& echo Docker URL: $DOCKER_URL \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/docker.tgz "${DOCKER_URL}" \  
&& ls -lha /tmp/docker.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& rm -rf /tmp/docker /tmp/docker.tgz \  
&& which docker \  
&& (docker version || true) \  
&& apk del .deps  
  
# Install docker-compose  
# https://docs.docker.com/compose/install/  
RUN set -x && \  
apk add --no-cache -t .deps ca-certificates curl && \  
DOCKER_COMPOSE_URL=https://github.com$(curl -L
https://github.com/docker/compose/releases/latest | grep -Eo
'href="[^"]+docker-compose-Linux-x86_64' | head -1 | sed 's/^href="//') && \  
curl -L $DOCKER_COMPOSE_URL -o /usr/local/bin/docker-compose && \  
chmod a+rx /usr/local/bin/docker-compose && \  
docker-compose version && \  
apk del .deps  
  
# Install bash & other utilities  
RUN apk add --no-cache bash gawk sed grep bc coreutils  
# Install AWSCLI  
RUN apk add --no-cache py-pip && pip install --no-cache-dir awscli  
# Install Dockerize  
ENV DOCKERIZE_VERSION v0.5.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
# Install HerokuCLI  
RUN npm install -g heroku-cli  

