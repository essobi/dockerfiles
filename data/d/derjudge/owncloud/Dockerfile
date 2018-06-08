FROM derjudge/archlinux-apache-php  
MAINTAINER Marc Richter <mail@marc-richter.info>  
  
RUN yes | pacman -Syy | cat  
RUN yes | pacman -S \  
cronie \  
exiv2 \  
ffmpeg \  
libreoffice-fresh \  
libx264 \  
owncloud \  
smbclient \  
| cat  
  
# Make owncloud configs  
ADD assets/config.php /etc/webapps/owncloud/config/config.php  
# Add write permission for httpd user  
RUN chmod g+w -R /usr/share/webapps/owncloud  
RUN chown http:http -R /etc/webapps/owncloud/config  
  
# Make httpd settings  
ADD assets/httpd.conf /etc/httpd/conf/httpd.conf  
ADD assets/owncloud.conf /etc/httpd/conf/owncloud.conf  
  
# Make PHP settings  
# Load PostgreSQL modules  
RUN sed -i'' 's#^;\\(extension=.*pgsql.*\\)#\1#g' /etc/php/php.ini  
# Load APCu module  
RUN sed -i'' 's#^;\\(extension=apcu.so\\)#\1#g' /etc/php/conf.d/apcu.ini  
# Load iconv module  
RUN sed -i'' 's#^;\\(extension=iconv.so\\)#\1#g' /etc/php/php.ini  
# Load posix module  
RUN sed -i'' 's#^;\\(extension=posix.so\\)#\1#g' /etc/php/php.ini  
# Load xmlrpc module  
RUN sed -i'' 's#^;\\(extension=xmlrpc.so\\)#\1#g' /etc/php/php.ini  
# Load bz2 module  
RUN sed -i'' 's#^;\\(extension=bz2.so\\)#\1#g' /etc/php/php.ini  
# Load intl module  
RUN sed -i'' 's#^;\\(extension=intl.so\\)#\1#g' /etc/php/php.ini  
# Load mcrypt module  
RUN sed -i'' 's#^;\\(extension=mcrypt.so\\)#\1#g' /etc/php/php.ini  
# Load openssl module  
RUN sed -i'' 's#^;\\(extension=openssl.so\\)#\1#g' /etc/php/php.ini  
# Un-Load mysqli module  
RUN sed -i'' 's#^\\(extension=mysqli.so\\)#;\1#g' /etc/php/php.ini  
# Load exif module  
RUN sed -i'' 's#^;\\(extension=exif.so\\)#\1#g' /etc/php/php.ini  
  
# Cronjob  
RUN if [ -f /extra/http.crontab ]; then crontab -u http /extra/http.crontab ;
fi  
  
# Add default extra - script  
RUN if [ ! -e /extra ]; then mkdir /extra; fi  
ADD assets/extra/init /extra/init  
RUN chmod +x /extra/init  
  
VOLUME ["/etc/webapps/owncloud"]  
  
# Create owncloud data dir  
RUN mkdir -p /var/lib/owncloud && \  
chown http:http -R /var/lib/owncloud  
  
VOLUME ["/var/lib/owncloud"]  
EXPOSE 80  
CMD ["/init"]  

