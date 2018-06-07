FROM lazyguru/mage2base  
  
# Installing PHP 7.0  
RUN yum -y install http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum -y install https://mirror.webtatic.com/yum/el6/latest.rpm  
RUN yum -y install php70w-pecl-memcache php70w-fpm php70w-intl php70w-mcrypt
php70w-mbstring php70w-mysql php70w-pdo php70w-mbstring php70w-soap
php70w-pecl-zendopcache php70w-xml php70w-gd php70w-opcache php70w-pecl-
imagick php70w-bcmath  
# <\---- End  
# php  
ADD etc/php.conf/php.ini /etc/php.ini  
  
# php fpm  
RUN mv /etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf.default  
ADD etc/php-fpm.conf/www.conf /etc/php-fpm.d/www.conf  
RUN mkdir -p /var/lib/php/session  
RUN mkdir -p /var/lib/php/wsdlcache  
RUN chmod -R 777 /var/lib/php/session  
RUN chmod -R 777 /var/lib/php/wsdlcache  
  
VOLUME ["/var/www/html"]  
  
EXPOSE 9001  
  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

