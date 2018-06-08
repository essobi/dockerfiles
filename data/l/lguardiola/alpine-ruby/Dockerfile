FROM lguardiola/alpine-ruby:2.4  
MAINTAINER Luis E. Guardiola <lguardiola@gmail.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN dep install  

