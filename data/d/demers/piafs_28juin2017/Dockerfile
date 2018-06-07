# Installation de Piwigo 2.9.1  
# Installation des plugins Community et Charlies  
# docker run --name mysql-piafs-data -d mysql false  
# docker run -d --name piafs-data demers/piafs-24juin2017 false  
# docker run --volumes-from mysql-piafs-data --name mysql-piafs -e
MYSQL_USER=piafs -e MYSQL_PASSWORD=piafs -e MYSQL_DATABASE=piafs -e
MYSQL_ROOT_PASSWORD=piafs -d mysql  
# docker run -d --volumes-from piafs-data --link mysql-piafs:mysql -p 80:80
demers/piafs-24juin2017  
  
FROM ubuntu:16.04  
ENV HOME /root  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install apache2 libapache2-mod-php7.0 -y  
ADD apache.sh /apache.sh  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_SERVER_NAME **NONE**  
RUN apt-get update && \  
apt-get install -y php7.0-mysql php7.0-gd imagemagick wget unzip mediainfo
ffmpeg && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# wget -q -O piafs.zip https://github.com/linuq/PIAFS/archive/master.zip && \  
# wget -q -O piwigo.zip http://piwigo.org/download/dlcounter.php?code=latest
&& \  
wget -q -O piwigo.zip http://piwigo.org/download/dlcounter.php?code=2.9.1 && \  
unzip piwigo.zip && \  
mv piwigo/* /var/www/html && \  
# Installation du plugin Community
http://fr.piwigo.org/ext/extension_view.php?eid=303  
wget -q -O community.zip http://fr.piwigo.org/ext/download.php?rid=6346 && \  
unzip -q community.zip -d /var/www/html/plugins/ && \  
# Installation du plugin Charlies
http://fr.piwigo.org/ext/extension_view.php?eid=119  
wget -q -O charlies.zip http://fr.piwigo.org/ext/download.php?rid=6143 && \  
unzip -q charlies.zip -d /var/www/html/plugins/ && \  
# Aller chercher les plugins faits par les étudiants à l'hiver 2017.  
wget -q -O plugins_etudiants.zip
https://github.com/linuq/PIAFS/archive/master.zip && \  
unzip -q plugins_etudiants.zip -d /tmp/ && \  
cp -R /tmp/PIAFS-master/src/plugins/LocalFilesEditor /var/www/html/plugins/ &&
\  
cp -R /tmp/PIAFS-master/src/plugins/editText /var/www/html/plugins/ && \  
cp -R /tmp/PIAFS-master/src/plugins/medicMonitor /var/www/html/plugins/ && \  
cp -R /tmp/PIAFS-master/src/plugins/editText /var/www/html/plugins/ && \  
cp -R /tmp/PIAFS-master/src/plugins/userInfo /var/www/html/plugins/ && \  
rm -f -r /tmp/PIAFS-master && \  
chown -R www-data:www-data /var/www/html && \  
rm -f piwigo.zip community.zip charlies.zip plugins_etudiants.zip && \  
chmod +x /apache.sh && \  
rm -f /var/www/html/index.html  
VOLUME ["/var/www/html/galleries", "/var/www/html/themes",
"/var/www/html/plugins", "/var/www/html/local"]  
EXPOSE 80  
CMD ["/apache.sh"]

