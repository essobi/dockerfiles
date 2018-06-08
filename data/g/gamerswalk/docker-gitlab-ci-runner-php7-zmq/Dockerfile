# docker-gitlab-ci-runner-php7-zmq  
FROM bobey/docker-gitlab-ci-runner-php7  
MAINTAINER Rodrigo Fandiño "rodrigo.fandino@gamerswalk.com"  
ENV PHP_VERSION 7.0.4  
RUN phpenv global $PHP_VERSION  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libzmq5 libzmq-dev php-
zmq  
RUN DEBIAN_FRONTEND=noninteractive curl -sL
https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs  

