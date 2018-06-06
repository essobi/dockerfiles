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
  
# Add NodeJS  
RUN apk add nodejs@community  
  
# Upgrade NPM  
RUN npm install -g npm  
  
# Copy app dependencies reference files  
COPY /whiteboard/package.json /whiteboard/package.json  
  
# Install app dependencies  
WORKDIR /whiteboard  
RUN npm install  
  
# Install LocalTunnel Module  
RUN npm install -g localtunnel  
  
# Expose Internal Port  
EXPOSE 4000  
# Eliminate Build Files  
# RUN npm uninstall -g npm  
RUN rm -rf /var/cache/apk/*  
  
# Define ENTRYPOINT  
# ENTRYPOINT [ "npm", "start" ]

