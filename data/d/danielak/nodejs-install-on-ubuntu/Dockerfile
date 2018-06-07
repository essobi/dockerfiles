FROM ubuntu:xenial-20170119  
# install a basic build chain  
RUN apt-get update && apt-get build-dep --assume-yes nodejs  
  
# install nodeJS as specified in  
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs

