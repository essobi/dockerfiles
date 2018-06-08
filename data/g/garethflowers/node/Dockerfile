FROM node:10.3.0-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.cmd="docker run -d -p 80:80 -v $PWD:/usr/src/app
garethflowers/node" \  
org.label-schema.description="Base image for a Node application" \  
org.label-schema.name="node" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.url="https://nodejs.org" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/garethflowers/docker-node" \  
org.label-schema.vendor="garethflowers" \  
org.label-schema.version="10.3.0"  
  
VOLUME [ "/usr/src/app" ]  
WORKDIR /usr/src/app  
  
RUN apk update \  
&& apk upgrade \  
&& rm -fr /var/cache/apk/* \  
&& npm install --global npm  

