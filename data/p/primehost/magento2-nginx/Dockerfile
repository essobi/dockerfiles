FROM primehost/nginx  
MAINTAINER Kevin Nordloh <mail@legendary-server.de>  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# install composer  
RUN apt-get -y install composer php7.0-soap  
  
# higher max_input_vars  
RUN sed -i -e "s/; max_input_vars\s*=\s*1000/max_input_vars = 1000000/g"
/etc/php/7.0/fpm/php.ini  
  
# clean up unneeded packages  
RUN apt-get \--purge autoremove -y  
  
# custom settings for magento2  
ADD ./nginx-default.conf /etc/nginx/sites-available/default  
  
# magento2 initialization and startup script  
ADD ./magento2-start.sh /root/container-scripts/prime-host/magento2-start.sh  
RUN chmod 755 /root/container-scripts/prime-host/magento2-start.sh  
  
CMD ["/bin/bash", "/root/container-scripts/prime-host/magento2-start.sh"]  

