FROM lakoo/node-alpine-gcloud:latest  
MAINTAINER William Chong <williamchong@lakoo.com>  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 17.03.0-ce  
ENV DOCKER_SHA256
4a9766d99c6818b2d54dc302db3c9f7b352ad0a80a2dc179ec164a3ba29c2d3e  
  
RUN apk add --no-cache curl openssl \  
&& set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& apk del curl openssl  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

