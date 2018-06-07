FROM ubuntu:16.04  
MAINTAINER Madhu Akula <madhu.akula@hotmail.com>  
  
RUN apt-get update && apt-get install ruby ruby-dev rubygems gcc make -y && \  
gem install --no-ri --no-rdoc fpm  
  
ENTRYPOINT [ "fpm" ]  
  
CMD [ "--help" ]  

