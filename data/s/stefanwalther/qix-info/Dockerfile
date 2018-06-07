# -------------------------------------------------------------------  
# BASE NODE  
# -------------------------------------------------------------------  
# We need full node as we need git to download from some GitHub repos.  
# -------------------------------------------------------------------  
FROM
node:8.11.2@sha256:321655aeb195b7946e9a29d28453388751389e8ced66b4dea772ae76a6985309
as BASE  
MAINTAINER Stefan Walther <swr-nixda@gmail.com>  
  
ARG BASE_VERSION="0.1.1"  
WORKDIR /opt/qix-info  
  
RUN npm install qix-info@$BASE_VERSION -g  
  
## -------------------------------------------------------------------  
## RELEASE  
## -------------------------------------------------------------------  
FROM
node:8.11.2-alpine@sha256:04d1f711703472ccb4ddc6bc9835ac0bcfc8afa4389534152d137ab93c24474a
as RELEASE  
  
RUN apk update  
RUN apk add bash  
  
# Enables colored output  
ENV FORCE_COLOR=true  
  
WORKDIR /opt/qix-info  
  
# OK, here we have to copy the symbolic link  
# use npm config get prefix to get the node.js prefix
https://stackoverflow.com/questions/18383476/how-to-get-the-npm-global-path-
prefix  
# Create the symbolic link  
RUN ln -s /usr/local/lib/node_modules/qix-info/bin/cli.js /usr/local/bin/qix-
info  
  
# Copy the global packages previously being installed  
COPY \--from=BASE /usr/local/lib/node_modules /usr/local/lib/node_modules  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

