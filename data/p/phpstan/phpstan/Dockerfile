FROM phpstan/phpstan:base  
MAINTAINER Tommy Muehle <tommy.muehle@gmail.com>  
  
ENV PHPSTAN_VERSION 0.6.x  
  
RUN composer global require phpstan/phpstan ^0.6 \  
&& composer global show | grep phpstan  

