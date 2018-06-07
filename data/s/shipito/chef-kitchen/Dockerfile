FROM docker:latest  
MAINTAINER Patrik Votocek <patrik@votocek.cz>  
  
# Install Chef Docker Kitchen  
RUN set -ex && \  
apk add --no-cache build-base ruby ruby-dev libffi-dev git openssh && \  
gem install chef berkshelf test-kitchen kitchen-docker io-console --no-
document  

