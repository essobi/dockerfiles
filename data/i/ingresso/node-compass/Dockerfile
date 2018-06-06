FROM node:slim  
MAINTAINER Danilo Tuler <danilo.tuler@b2wdigital.com>  
  
# install ruby and compass  
RUN apt-get update -y && apt-get -y -q install gcc make ruby ruby-dev libxml2
libxml2-dev libxslt1-dev git bzip2 && gem install compass  
  
# fix bower problems when running from docker (or http proxy)  
# http://stackoverflow.com/questions/1722807/git-convert-git-urls-to-http-urls  
#RUN git config --global url.https://github.com/.insteadOf git://github.com/  

