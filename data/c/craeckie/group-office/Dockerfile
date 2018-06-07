FROM craeckie/webbase  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libpspell-dev \  
libxml2-dev \  
zlib1g-dev  
  
RUN docker-php-ext-install mysqli pdo_mysql mcrypt pspell calendar xml
mbstring zip shmop  
  
ENV go_config /root/group-office-config.php  
  
RUN mkdir -p /home/groupoffice/  
RUN chown www-data:www-data /home/groupoffice/  
  
WORKDIR /root  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
ADD group-office-config.php $go_config  
  
CMD ["bash", "/root/init.sh"]  

