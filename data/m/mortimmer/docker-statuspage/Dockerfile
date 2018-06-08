FROM node:alpine  
  
# install docker  
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
  
# setup project  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
RUN npm install  
  
CMD npm start

