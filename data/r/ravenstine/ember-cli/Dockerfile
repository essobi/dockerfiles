FROM node:7.10.1-alpine  
  
# Why not Node 8.0?  
# Because the Node 8.0 alpine image comes with NPM 5.0, which has  
# issues running in Docker and even CircleCI.  
#  
# https://discuss.circleci.com/t/npm-install-error-that-isnt-reproducing-in-a-
local-docker-container/13085  
#  
# https://github.com/npm/npm/issues/17578  
#  
  
USER root  
  
RUN apk update && apk add \--no-cache \  
git  
  
ENV HOME /root  
  
VOLUME /root  
  
WORKDIR $HOME  
  
ENV PATH="${HOME}/bin:${PATH}"  
# Install ember dev dependencies  
RUN npm install -g bower@1.8.0 phantomjs-prebuilt@2.1.7 ember-cli@2.14.0  
  
CMD /bin/sh  
  

