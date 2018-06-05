FROM ruby:2.4-alpine3.6  
MAINTAINER Lucio Delelis <ldelelis@est.frba.utn.edu.ar>  
  
RUN mkdir /usr/src/app  
  
COPY . /usr/src/app  
  
WORKDIR /usr/src/app  
  
RUN apk update && \  
apk add ruby-dev build-base curl-dev && \  
bundle install --deployment && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["./botsuki.rb"]  

