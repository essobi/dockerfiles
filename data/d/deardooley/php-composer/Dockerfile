######################################################  
#  
# PHP 5.6 \+ Composer  
# Tag: deardooley/php:5.6-composer  
#  
# This is a minimal alpine-based php 5.6 image with  
# Apache 2.4 and composer installed.  
#  
######################################################  
  
FROM deardooley/php:5.6  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer about  

