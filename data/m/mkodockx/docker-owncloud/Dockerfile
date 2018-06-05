FROM mkodockx/docker-lamp  
MAINTAINER mko <code@m-ko-x.de>  
  
ENV MAX_UPLOAD_SIZE 5G  
  
# install deps  
RUN pacman -Sy && \  
pacman -S --noconfirm --needed smbclient ffmpeg libreoffice-fresh nano msmtp
msmtp-mta openssl  
  
# packaged core and apps  
RUN pacman -S --noconfirm --needed owncloud && \  
pacman -S --noconfirm --needed owncloud-app-bookmarks \  
owncloud-app-calendar \  
owncloud-app-contacts \  
owncloud-app-documents \  
owncloud-app-gallery  
  
# prepare container permission updater  
ADD ./permissions/perms-container.sh /perms.sh  
RUN chmod -R a+x /perms.sh  
  
# enable large file uploads  
RUN sed -i "s,php_value upload_max_filesize 513M,php_value upload_max_filesize
${MAX_UPLOAD_SIZE},g" /usr/share/webapps/owncloud/.htaccess && \  
sed -i "s,php_value post_max_size 513M,php_value post_max_size
${MAX_UPLOAD_SIZE},g" /usr/share/webapps/owncloud/.htaccess && \  
sed -i 's,<IfModule mod_php5.c>,<IfModule mod_php5.c>\nphp_value
output_buffering Off,g' /usr/share/webapps/owncloud/.htaccess  
  
# apache setup  
RUN cp /etc/webapps/owncloud/apache.example.conf
/etc/httpd/conf/extra/owncloud.conf && \  
sed -i '/<VirtualHost/,/<\/VirtualHost>/d' /etc/httpd/conf/extra/owncloud.conf
&& \  
sed -i 's,Options Indexes FollowSymLinks,Options -Indexes +FollowSymLinks,g'
/etc/httpd/conf/httpd.conf && \  
sed -i '$a Include conf/extra/owncloud.conf' /etc/httpd/conf/httpd.conf && \  
chown -R http:http /usr/share/webapps/owncloud/  
  
# configure PHP open_basedir  
RUN sed -i
's,^open_basedir.*$,\0:/usr/share/webapps/owncloud/:/usr/share/webapps/owncloud/config/:/etc/webapps/owncloud/config/,g'
/etc/php/php.ini  
  
# apps from store  
RUN mkdir -p /usr/share/webapps/owncloud/apps  
ADD ./apps.tar.gz /usr/share/webapps/owncloud/apps/  
  
# handle custom subpathing  
ENV OC_PATH ""  
RUN sed -i 's,Alias /owncloud /usr/share/webapps/owncloud/,Alias /${OC_PATH}
/usr/share/webapps/owncloud/,g' /etc/httpd/conf/extra/owncloud.conf  
  
# prepare encryption  
RUN sed -i 's,;extension=openssl.so,extension=openssl.so,g' /etc/php/php.ini
&& \  
sed -i 's,#LoadModule ssl_module modules/mod_ssl.so,LoadModule ssl_module
modules/mod_ssl.so,g' /etc/httpd/conf/httpd.conf && \  
sed -i 's,#LoadModule socache_shmcb_module
modules/mod_socache_shmcb.so,LoadModule socache_shmcb_module
modules/mod_socache_shmcb.so,g' /etc/httpd/conf/httpd.conf  
  
# run it  
RUN /perms.sh  
CMD ["/opt/boot.sh"]

