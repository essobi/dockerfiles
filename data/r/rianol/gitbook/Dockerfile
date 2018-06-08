FROM node:8-alpine  
  
LABEL maintainer="Rianol Jou <rianol.jou@gmail.com>"  
  
RUN apk update &&\  
apk upgrade &&\  
apk add git openjdk8-jre graphviz &&\  
npm install -g gitbook-cli &&\  
gitbook fetch &&\  
rm -rf /tmp/*  
  
ENV BOOKDIR /gitbook  
  
VOLUME $BOOKDIR  
  
EXPOSE 4000  
WORKDIR $BOOKDIR  
  
ENTRYPOINT ["/usr/local/bin/gitbook"]  

