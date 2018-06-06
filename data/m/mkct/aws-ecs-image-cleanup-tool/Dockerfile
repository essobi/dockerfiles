FROM alpine:3.3  
RUN apk add --no-cache curl  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.9.1  
ENV DOCKER_SHA256
6a095ccfd095b1283420563bd315263fa40015f1cee265de023efef144c7e52d  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& rm docker.tgz \  
&& docker -v  
  
WORKDIR /cleanup  
  
COPY . /cleanup  
  
CMD ["./cmd.sh"]  

