FROM php:7.1-alpine  
MAINTAINER Anton Orlov <anton@pinked.ru>  
  
ENV BEANSTALK_SERVERS beanstalkd:11300  
RUN cd /home \  
&& curl -sL
https://github.com/ptrofimov/beanstalk_console/archive/master.tar.gz | tar -xz
\  
&& mv beanstalk_console-master source  
  
EXPOSE 2080  
CMD ["php", "-S", "0.0.0.0:2080", "-t", "/home/source/public"]

