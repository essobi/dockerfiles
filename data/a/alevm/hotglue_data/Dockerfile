MAINTAINER levm "av@levm.eu"  
FROM ubuntu  
RUN apt-get install git -y  
RUN git clone git://github.com/hotglue/hotglue2.git -b dev
/var/www/html/hotglue  
RUN chmod -R 0777 /var/www/html/hotglue/content  
ADD user-config.inc.php /var/www/html/hotglue/user-config.inc.php  
RUN mv /var/www/html/hotglue/htaccess-dist /var/www/html/hotglue/.htaccess  
VOLUME /var/www/html  
CMD ["true"]  

