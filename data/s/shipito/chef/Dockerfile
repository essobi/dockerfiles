FROM alpine:latest  
MAINTAINER Patrik Votocek <patrik@votocek.cz>  
  
# Install Chef Docker Kitchen  
RUN set -ex && \  
apk add --no-cache build-base ruby ruby-dev libffi-dev libxml2-dev git openssh
&& \  
gem install chef berkshelf foodcritic rubocop rake rspec chefspec io-console
\--no-document  

