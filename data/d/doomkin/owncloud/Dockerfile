#  
# doomkin/owncloud Dockerfile  
#  
# Build: sudo docker build -t doomkin/owncloud .  
# mkdir ~/ocfiles  
# chmod -R 770 ~/ocfiles; sudo chgrp -R 33 ~/ocfiles  
# sudo chcon -Rt svirt_sandbox_file_t ~/ocfiles  
#  
# Run: sudo docker run --name ownc -v ~/ocfiles:/var/www/owncloud/data -P -it
-d doomkin/owncloud  
#  
# Login: eval `ssh-agent -s`; ssh-add ssh/id_rsa; ssh root@localhost -p `sudo
docker port ownc 22 | cut -d":" -f2`  
#  
  
FROM doomkin/ubuntu-ssh  
MAINTAINER Pavel Nikitin <p.doomkin@ya.ru>  
  
# Set the noninteractive frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install owncloud  
RUN echo 'deb
http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.04/
/' >> /etc/apt/sources.list.d/owncloud.list; \  
wget
http://download.opensuse.org/repositories/isv:ownCloud:community/xUbuntu_14.04/Release.key;
\  
apt-key add - < Release.key; \  
apt-get update; \  
apt-get install -y owncloud; \  
apt-get clean; \  
rm -f Release.key; \  
service mysql start; \  
echo "mysqladmin --silent --wait=30 ping || exit 1" > config; \  
echo "mysql -e 'CREATE DATABASE owncloud CHARACTER SET utf8 COLLATE
utf8_general_ci;'" >> config; \  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"localhost\" WITH
GRANT OPTION;'" >> config; \  
echo "mysqladmin -u root password secret" >> config; \  
bash config; \  
rm -f config; \  
service mysql stop; \  
sed -i 's,php_value upload_max_filesize 513M,php_value upload_max_filesize
30G,g' /var/www/owncloud/.htaccess; \  
sed -i 's,php_value post_max_size 513M,php_value post_max_size 30G,g'
/var/www/owncloud/.htaccess; \  
sed -i 's,<IfModule mod_php5.c>,<IfModule mod_php5.c>\nphp_value
output_buffering Off,g' /var/www/owncloud/.htaccess; \  
sed -i 's,;default_charset = "UTF-8",default_charset = "UTF-8",g'
/etc/php5/apache2/php.ini; \  
sed -i 's,max_file_uploads = 20,max_file_uploads = 200,g'
/etc/php5/apache2/php.ini; \  
chown -R www-data:www-data /var/www; \  
sed -i 's/^exit 0/service apache2 start\nservice mysql start\nexit 0/'
/etc/rc.local  
  
VOLUME /var/www/owncloud/data  
  
EXPOSE 80 443  
# Default command  
CMD /etc/rc.local; bash  

