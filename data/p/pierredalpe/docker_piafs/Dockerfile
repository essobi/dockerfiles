# Installation de Piwigo 2.9.1  
# Installation des plugins Community et Charlies  
  
FROM ubuntu:16.04  
  
ENV APACHE_RUN_USER='www-data' \  
APACHE_RUN_GROUP='www-data' \  
APACHE_SERVER_NAME='**NONE**' \  
DB_PASS='piafs-db-pass' \  
DB_USER='piafs-db-user' \  
DB_NAME='piafs-db-name' \  
DB_HOST='mysql' \  
HOME='/root' \  
PIAFS_UID='1000' \  
PIAFS_GID='1000' \  
APACHE_PID_FILE='/var/run/apache2/apache2.pid' \  
APACHE_RUN_DIR='/var/run/apache2' \  
DEBIAN_FRONTEND='noninteractive'  
  
ADD rootfs/ /  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
apache2 \  
duplicity \  
ffmpeg \  
imagemagick \  
libapache2-mod-php7.0 \  
mediainfo \  
mysql-client \  
php7.0-gd \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-xml \  
unzip \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& wget -q -O piwigo.zip http://piwigo.org/download/dlcounter.php?code=latest
\  
&& unzip piwigo.zip \  
&& mv piwigo/* /var/www/html  
# Installation du plugin Community
http://fr.piwigo.org/ext/extension_view.php?eid=303  
RUN wget -q -O community.zip http://fr.piwigo.org/ext/download.php?rid=6346 \  
&& unzip -q community.zip -d /var/www/html/plugins/ \  
# Installation du plugin Charlies
http://fr.piwigo.org/ext/extension_view.php?eid=119  
&& wget -q -O charlies.zip http://fr.piwigo.org/ext/download.php?rid=6143 \  
&& unzip -q charlies.zip -d /var/www/html/plugins/ \  
# Aller chercher les plugins faits par les étudiants à l'hiver 2017.  
&& wget -q -O plugins_etudiants.zip
https://github.com/linuq/PIAFS/archive/master.zip \  
&& unzip -q plugins_etudiants.zip -d /tmp/ \  
&& cp -R /tmp/PIAFS-master/src/plugins/LocalFilesEditor /var/www/html/plugins/
\  
&& cp -R /tmp/PIAFS-master/src/plugins/editText /var/www/html/plugins/ \  
&& cp -R /tmp/PIAFS-master/src/plugins/medicMonitor /var/www/html/plugins/ \  
&& cp -R /tmp/PIAFS-master/src/plugins/editText /var/www/html/plugins/ \  
&& cp -R /tmp/PIAFS-master/src/plugins/userInfo /var/www/html/plugins/ \  
&& rm -f -r /tmp/PIAFS-master \  
&& chown -R www-data:www-data /var/www/html \  
&& rm -f piwigo.zip community.zip charlies.zip plugins_etudiants.zip \  
&& chmod +x /entrypoint.sh \  
&& chmod +x /backup.sh \  
&& chmod +x /restore.sh \  
&& rm -f /var/www/html/index.html  
  
VOLUME ["/var/www/html/galleries", "/var/www/html/themes",
"/var/www/html/plugins", "/var/www/html/local", "/var/www/html/upload",
"/backups"]  
  
EXPOSE 80  
  
CMD ["/entrypoint.sh"]  

