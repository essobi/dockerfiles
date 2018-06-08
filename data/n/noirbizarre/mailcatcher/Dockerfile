FROM ruby:2.2-alpine  
MAINTAINER Axel Haustant "noirbizarre@gmail.com"  
ENV MAILCATCHER_VERSION 0.6.4  
RUN apk add --update --no-cache sqlite-dev libstdc++  
  
RUN apk --update add --no-cache --virtual build_deps build-base && \  
gem install mailcatcher -v $MAILCATCHER_VERSION \--no-rdoc --no-ri && \  
apk del build_deps  
  
EXPOSE 1025 1080  
CMD ["mailcatcher", "--smtp-ip=0.0.0.0", "--http-ip=0.0.0.0", "--foreground"]  

