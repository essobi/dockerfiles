# -------------------------------------------------------------------  
# BASE NODE  
# -------------------------------------------------------------------  
# We need full node as we need git to download from some GitHub repos.  
# -------------------------------------------------------------------  
FROM node:8.6.0 as BASE  
MAINTAINER Stefan Walther <swr-nixda@gmail.com>  
  
ARG SENSE_GO_VERSION="0.14.6"  
WORKDIR /opt/sense-go  
  
RUN npm install sense-go@$SENSE_GO_VERSION -g  
  
## -------------------------------------------------------------------  
## RELEASE  
## -------------------------------------------------------------------  
FROM node:8.6.0-alpine as RELEASE  
  
RUN apk update  
RUN apk add bash  
  
WORKDIR /opt/sense-go  
  
# Enables colored output  
ENV FORCE_COLOR=true  
  
# OK, here we have to copy the symbolic link  
# use npm config get prefix to get the node.js prefix
https://stackoverflow.com/questions/18383476/how-to-get-the-npm-global-path-
prefix  
# Create the symbolic link  
RUN ln -s /usr/local/lib/node_modules/sense-go/bin/cli.js
/usr/local/bin/sense-go  
  
# Copy the global packages previously being installed  
COPY \--from=BASE /usr/local/lib/node_modules /usr/local/lib/node_modules  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

