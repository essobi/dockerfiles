FROM php:7-alpine  
  
ENV REFRESHED_AT="2017-05-22"  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
ADD docroot /docroot  
  
CMD ["php", "-S", "0.0.0.0:9000", "-t", "/docroot", "docroot/index.php"]  

