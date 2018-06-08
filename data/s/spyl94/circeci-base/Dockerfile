FROM alpine:3.4  
MAINTAINER Aurélien David  
  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
openssl  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.13.0  
ENV DOCKER_SHA256
fc194bb95640b1396283e5b23b5ff9d1b69a5e418b5b3d774f303a7642162ad6  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN apk add --no-cache \  
git \  
openssh-client  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
py-yaml \  
build-base \  
&& pip install virtualenv 'docker-compose==1.8.0' \  
&& rm -rf /var/cache/apk/*  
  
RUN apk add --no-cache curl rsync openssh &&\  
apk add --no-cache fabric --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

