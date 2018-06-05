FROM python:alpine  
  
ENV DOCKER_CHANNEL edge  
ENV DOCKER_VERSION 17.05.0-ce  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz";
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
rm docker.tgz; \  
apk del .fetch-deps; \  
dockerd -v; \  
docker -v  
  
RUN set -xe && \  
apk add --no-cache tar git openssh-client && \  
pip install awscli boto yamllint && \  
true  
  
RUN set -xe && \  
apk add --no-cache ansible && \  
true  
  
COPY bin /usr/local/bin  
COPY config.json /root/.docker/config.json  

