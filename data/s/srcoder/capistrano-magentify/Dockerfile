FROM ruby:alpine  
MAINTAINER Jeroen Boersma <jeroen@srcode.nl>  
  
RUN apk add --no-cache make g++ openssh-client libcurl curl-dev && \  
gem install -n /usr/local/bin magentify json curb colored nokogiri sshkit
capistrano && \  
apk del make g++ curl-dev  
  
WORKDIR /app  
  
CMD ["/usr/local/bin/cap"]  

