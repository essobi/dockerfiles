# Build:  
# docker build -t webclub/omt .  
#  
# Run:  
# docker run -it webclub/omt  
#  
# Compose:  
# docker-compose up -d  
# FROM node:argon  
FROM ubuntu:latest  
MAINTAINER Ho Minh Chung <hmchung@tma.com.vn>  
  
# Install Utilities  
RUN apt-get update -q  
RUN apt-get install -yqq wget aptitude htop vim git traceroute dnsutils curl
ssh sudo tree tcpdump nano psmisc gcc make build-essential libfreetype6
libfontconfig libkrb5-dev  
  
# Sets up labels for the source code commit badge  
ARG VCS_REF  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="e.g. https://github.com/microscaling/microscaling"  
  
# Metadata params  
ARG VERSION  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor="Microscaling Systems" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.url="https://bitbucket.org/webclubtma/overtime-management-
tool" \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile"  
  
# Install gem sass for grunt-contrib-sass  
RUN apt-get install -y ruby  
RUN gem install sass  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN sudo apt-get install -yq nodejs  
  
# Install omt Prerequisites  
RUN npm install --quiet -g grunt-cli gulp bower yo mocha karma-cli pm2  
  
RUN mkdir /opt/omt  
RUN mkdir -p /opt/omt/public/lib  
WORKDIR /opt/omt  
  
# Copies the local package.json file to the container  
# and utilities docker container cache to not needing to rebuild  
# and install node_modules/ everytime we build the docker, but only  
# when the local package.json file changes.  
# Install npm packages  
ADD package.json /opt/omt/package.json  
RUN npm install --quiet --F  
  
# Install bower packages  
ADD bower.json /opt/omt/bower.json  
ADD .bowerrc /opt/omt/.bowerrc  
RUN bower install --quiet --allow-root --config.interactive=false -F  
# Share local directory on the docker container  
ADD . /opt/omt  
  
# Machine cleanup  
RUN npm cache clean  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set development environment as default  
ENV NODE_ENV development  
  
# Ports generic  
EXPOSE 80:80  
EXPOSE 443:443  
# Port 3000 for omt server  
EXPOSE 3000:3000  
# Port 5858 for node debug  
EXPOSE 5858:5858  
# Port 35729 for livereload  
EXPOSE 35729:35729  
# Run omt server  
CMD ["grunt", "serve"]  

