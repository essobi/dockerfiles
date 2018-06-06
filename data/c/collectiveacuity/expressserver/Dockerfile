FROM alpine:edge  
  
MAINTAINER <support@collectiveacuity.com>  
  
# Update Alpine environment  
RUN apk update  
RUN apk upgrade  
RUN apk add ca-certificates  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories  
RUN echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories  
RUN apk update  
RUN apk upgrade  
  
# Add NodeJS & NPM  
RUN apk add nodejs@community  
  
# Copy Server Dependencies  
COPY /server/package.json /server/package.json  
  
# Install Server dependencies  
WORKDIR /server  
RUN npm install  
  
# Install LocalTunnel Module  
RUN npm install -g localtunnel  
  
# Expose Internal Port  
EXPOSE 8080  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
  
# Define ENTRYPOINT  
# ENTRYPOINT [ "node", "server.js" ]  

