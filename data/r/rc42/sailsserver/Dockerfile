FROM alpine:edge  
  
MAINTAINER <richard@collectiveacuity.com>  
  
# Update Alpine environment  
RUN apk update  
RUN apk upgrade  
RUN apk add ca-certificates  
RUN rm -rf /var/cache/apk/*  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories  
RUN echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories  
RUN apk update  
RUN apk upgrade  
  
# Add NodeJS  
RUN apk add nodejs@community  
  
# Upgrade NPM  
RUN npm install -g npm  
  
# Copy app dependencies reference files  
COPY /server/app.js /server/app.js  
COPY /server/Gruntfile.js /server/Gruntfile.js  
COPY /server/.sailsrc /server/.sailsrc  
COPY /server/package.json /server/package.json  
  
# Install app dependencies  
WORKDIR /server  
RUN npm install  
  
# Install LocalTunnel Module  
RUN npm install -g localtunnel  
  
# Expose Internal Port  
EXPOSE 1337  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
  
# Define ENTRYPOINT  
# ENTRYPOINT [ "node", "app.js" ]  

