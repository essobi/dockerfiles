FROM gongo/emacs  
  
MAINTAINER Wataru MIYAGUNI <gonngo@gmail.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Cask /usr/src/app/  
ONBUILD RUN cask install  
ONBUILD COPY . /usr/src/app/  

