# Dockerfile for chruby  
# we're running this on ubuntu:latest  
FROM ubuntu:latest  
# adding a maintainer tagline  
MAINTAINER Hallaj <hallaj@inu.io>  
# setting noninteractive frontend  
ENV DEBIAN_FRONTEND noninteractive  
# refresh apt-cache  
RUN apt-get -qq update  
# start by installing dependencies  
RUN apt-get -qq -y install build-essential wget  
# installation of chruby  
COPY /scripts/setup/chruby.sh /scripts/setup/chruby.sh  
RUN /scripts/setup/chruby.sh  
# installation of ruby-install  
COPY /scripts/setup/ruby-install.sh /scripts/setup/ruby-install.sh  
RUN /scripts/setup/ruby-install.sh  
# setting up rubies  
COPY /scripts/setup/rubies.sh /scripts/setup/rubies.sh  
RUN /scripts/setup/rubies.sh  
# final execution bit  
COPY /scripts/exec/run.sh /scripts/exec/run.sh  
CMD /scripts/exec/run.sh  

