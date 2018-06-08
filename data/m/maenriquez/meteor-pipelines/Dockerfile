FROM node:7.10.0-wheezy  
MAINTAINER Marc Enriquez  
  
# Install latest meteor version  
RUN curl -sL https://raw.githubusercontent.com/auterium/meteor-
pipelines/v1.2.0.2/install.sh | sed s/--progress-bar/-sL/g | /bin/sh  
RUN export METEOR_ALLOW_SUPERUSER=true  
  
RUN adduser --disabled-password --gecos '' docker_meteor  
USER docker_meteor  
RUN meteor npm install

