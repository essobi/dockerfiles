FROM piuma/centos7-apache-php  
  
# Update the base system to support some locales  
RUN yum update -y \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN sed -i \  
-e 's~^date.timezone = Europe/Rome$~date.timezone = Asia/Shanghai~g' \  
/etc/php.ini  
  
#Enable `AllowOverride All` for /var/www/html.  
# There is a .htaccess which enable ReWrite and other thing  
RUN sed -i '/<Directory \"\/var\/www\/html\">/,/<\/Directory>/ s/AllowOverride
None/AllowOverride All/' /etc/httpd/conf/httpd.conf  
  
ADD entrypoint.sh /entrypoint.sh  
  
CMD /entrypoint.sh  

