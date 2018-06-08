FROM tutum/lamp  
MAINTAINER Andrew Warren <andrew.warren@spectrakey.co.uk>  
  
RUN sh -c "echo 'deb
http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.10/
/' >> /etc/apt/sources.list.d/owncloud.list"  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 977C43A8BA684223  
  
RUN apt-get update  
  
RUN apt-get install owncloud -y  
  
# enable large file uploads by replacing php values in .htaccess  
RUN sudo sed -i 's#php_value upload_max_filesize 513M#php_value
upload_max_filesize 2G#g' /var/www/owncloud/.htaccess  
RUN sudo sed -i 's#php_value post_max_size 513M#php_value post_max_size 2G#g'
/var/www/owncloud/.htaccess  
RUN sudo sed -i '$a php_value output_buffering Off'
/var/www/owncloud/.htaccess  
  
# setup Apache for owncloud  
RUN sed -i '$a Include conf-enabled/owncloud.conf' /etc/apache2/apache2.conf  
RUN chown -R www-data:www-data /var/www/owncloud/  
RUN chown -R www-data:www-data /var/www/html/  
  
EXPOSE 8080  

