FROM debian:jessie  
  
MAINTAINER Martin Janser <martin@duss-janser.ch>  
  
RUN apt-get update && apt-get install -y rubygems git  
RUN gem install capifony -v 2.8.3  
  
ENV SSH_AUTH_SOCK /root/ssh-agent  
  
WORKDIR /root/workdir  
  
ENTRYPOINT ["cap"]  

