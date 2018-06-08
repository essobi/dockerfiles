# composer image  
# runs composer within a container  
FROM ubuntu:14.04  
MAINTAINER François Zaninotto <francois+docker@marmelab.com>  
  
ENV HOME /root  
  
RUN apt-get update -qq  
RUN apt-get install -y -qq git curl wget  
  
# install HHVM  
RUN wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add -  
RUN echo deb http://dl.hhvm.com/ubuntu trusty main | tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update -qq && apt-get install -y -qq hhvm  
RUN echo "date.timezone = Europe/Paris" >> /etc/hhvm/php.ini  
  
# install phpunit  
RUN wget -O /usr/local/bin/phpunit -q https://phar.phpunit.de/phpunit.phar  
  
WORKDIR /srv  
  
ENTRYPOINT ["hhvm", "/usr/local/bin/phpunit"]  

