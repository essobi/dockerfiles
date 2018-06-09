FROM node:alpine  
  
RUN apk --no-cache add curl && npm install -g stubby  
COPY ["scripts/*", "/scripts/"]  
WORKDIR /scripts  
CMD ["/bin/ash","set_stubs.sh"]

