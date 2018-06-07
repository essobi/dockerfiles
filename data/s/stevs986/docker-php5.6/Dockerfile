FROM ubuntu:16.04  
MAINTAINER Sladjan Nikolic <sladjan.nikolic986@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LC_ALL=C.UTF-8  
ADD . /scripts  
  
RUN chmod -R +x /scripts/  
RUN /scripts/prepare.sh  
  
EXPOSE 9000  
CMD /usr/sbin/php-fpm5.6 -F -R  
  

