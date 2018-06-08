FROM ubuntu:14.10  
MAINTAINER Rob Haswell <me@robhaswell.co.uk>  
  
RUN apt-get -qq update  
RUN apt-get -qqy upgrade  
  
RUN apt-get install -qqy git curl php5-cli php5-curl php-apc php5-mysql  
RUN git clone https://github.com/njam/github-salto.git  
  
WORKDIR /github-salto  
RUN curl -sS https://getcomposer.org/installer | php  
RUN php composer.phar install  
  
RUN adduser --system github_salto  
RUN mkdir data tmp  
RUN chown github_salto data tmp  
USER github_salto  
  
VOLUME /github-salto/data  
  
ENTRYPOINT ["bin/cm", "graph"]  

