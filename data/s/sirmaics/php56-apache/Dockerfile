FROM fbender/php56-apache-mysql  
  
RUN a2enmod ssl  
RUN a2enmod expires  
RUN a2enmod ext_filter  
RUN a2enmod headers  
RUN a2enmod remoteip  
RUN apt-get install php5-memcache php5-memcached php5-redis php5-tidy vim -y  

