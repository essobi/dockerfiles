FROM node:alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ENV INITVERSION 1.2.1  
LABEL Maintainer="Zaher Ghaibeh <z@zah.me>" \  
Description="Lightweight nodejs container based on alpine with bower, yarm,
gulp and typescript." \  
org.label-schema.name="Nodejs Toolkit" \  
org.label-schema.description="Lightweight nodejs container based on alpine
with bower, yarm, gulp and typescript." \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/linuxjuggler/node-toolkit-
apline.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0"  
  
RUN apk --no-cache update && apk --no-cache upgrade && apk add wget yarn && \  
apk --no-cache add ca-certificates && update-ca-certificates && \  
npm install -g gulp bower typescript && \  
npm cache verify && \  
wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${INITVERSION}/dumb-init_${INITVERSION}_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
  
WORKDIR /workspace  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  

