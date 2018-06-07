FROM ubuntu:16.04  
MAINTAINER Uday Bhanu Prasad <uday1bhanu@gmail.com>  
ENV REFRESHED_AT 2017-04-03  
RUN apt-get -yqq update; apt-get -yqq install ruby ruby-dev build-essential  
RUN gem install --no-ri --no-rdoc json  
  
RUN mkdir -p /opt/distributed_client  
ADD client.rb /opt/distributed_client  
  
WORKDIR /opt/distributed_client  
  
ENTRYPOINT [ "ruby", "/opt/distributed_client/client.rb" ]  
CMD []  

