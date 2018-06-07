FROM debian:latest  
  
MAINTAINER Jack Yu <jackysp@gmail.com>  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install gcc make ruby ruby-dev && \  
apt-get autoclean && \  
gem install jekyll redcarpet && \  
rm -rf /usr/lib/ruby/gems/*/cache/*.gem  
  
ENTRYPOINT ["jekyll"]  

