# This file is generated from ../Dockerfile.template.  
# To update this file run go to repo root and run './template.sh 8'.  
FROM node:8-alpine  
  
# @see http://label-schema.org/rc1/  
LABEL maintainer="Phase2 <outrigger@phase2technology.com>" \  
# Replacement for the old MAINTAINER directive has fragmented.  
org.label-schema.vendor="Phase2 <outrigger@phase2technology.com>" \  
org.label-schema.name="Node v8" \  
org.label-schema.vcs-url="https://github.com/phase2/docker-node" \  
org.label-schema.docker.cmd="docker run --rm -it outrigger/node:8" \  
org.label-schema.schema-version="1.0"  
# Operational node systems commonly need to make remote requests.  
RUN apk --update --no-cache add bash curl git openssl tini  
  
ENV \  
OUTRIGGER_QUIET=0 \  
# Build with NODE_ENV=development to include dev dependencies.  
NODE_ENV=production \  
# Align the npm cache with yarn for easier cache persistence by volumes.  
NPM_CONFIG_CACHE=/usr/local/share/.cache/npm \  
YARN_CACHE_FOLDER=/usr/local/share/.cache/yarn  
  
RUN mkdir /code && \  
mkdir -p /usr/local/share/.cache && \  
chown -R node:node /code && \  
chown -R node:node /usr/local/share/.cache  
  
COPY /root /  
  
# Set a non-root user. This user is created upstream but not set for use.  
USER node  
  
# Set working directory to the expected location of application code.  
WORKDIR /code/  
  
# Expose our service port. Node services should bind to this port.  
EXPOSE 3773  
  
# Lightweight init system for containers.  
# @see https://github.com/krallin/tini  
ENTRYPOINT ["/sbin/tini", "--"]  
  
# Use of exec replaces the BASH process with our node process  
# instead of spawning a second process.  
# @see https://en.wikipedia.org/wiki/Exec_(system_call)  
CMD ["bash", "-c", "/pre-start && exec node"]  

