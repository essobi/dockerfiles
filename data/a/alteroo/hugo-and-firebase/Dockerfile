FROM node:6.9.2-alpine  
  
ENV HUGO_VERSION 0.19  
ENV HUGO_TARBALL_NAME hugo_${HUGO_VERSION}_Linux-64bit  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64  
  
# Download hugo  
# no more ADD, hopefully reduce the docker layers  
# ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TARBALL_NAME}.tar.gz
/usr/local/  
# install firebase-tools and hugo in one command, makes for a smaller image  
# according to https://semaphoreci.com/blog/2016/12/13/lightweight-docker-
images-in-5-steps.html  
RUN npm install -g firebase-tools \  
&& apk add --update ca-certificates wget \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TARBALL_NAME}.tar.gz
\  
&& tar xzf ${HUGO_TARBALL_NAME}.tar.gz \  
&& mv ${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \  
&& rm ${HUGO_TARBALL_NAME}.tar.gz

