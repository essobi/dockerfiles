FROM mageinferno/magento2-php:5.6-fpm  
MAINTAINER Jhony Duenas <jduenas@thinkpyxl.com>  
  
ADD ./m2setup.sh /usr/local/bin/  
RUN usermod -u 1000 nginx  
RUN usermod -G staff nginx  
  
CMD ["/usr/local/bin/m2setup.sh"]

