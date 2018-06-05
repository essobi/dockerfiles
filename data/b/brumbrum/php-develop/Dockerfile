FROM brumbrum/php-phantomjs  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
RUN \  
apt-get -y --no-install-recommends install php-xdebug wget mysql-client
imagemagick exiftool php7.0-gd php7.0-imagick gphoto2 iw rfkill iproute2
wpasupplicant isc-dhcp-client && \  
mkdir -p /var/run/php && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  
  
# Configuro XDebug  
RUN \  
echo "xdebug.max_nesting_level = 250" >> /etc/php/7.0/fpm/php.ini && \  
echo "xdebug.remote_enable=on" >> /etc/php/7.0/fpm/php.ini && \  
echo "xdebug.remote_autostart=on" >> /etc/php/7.0/fpm/php.ini && \  
echo "xdebug.remote_host=172.17.0.1" >> /etc/php/7.0/fpm/php.ini && \  
echo "xdebug.remote_port=9001" >> /etc/php/7.0/fpm/php.ini && \  
echo "display_errors=on" >> /etc/php/7.0/fpm/php.ini  
  
ENV PHP_IDE_CONFIG serverName=docker  
  
# Installo SonarQube Scanner  
#
https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner#AnalyzingwithSonarQubeScanner-
Installation  
RUN \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.1.0.1141-linux.zip && \  
unzip sonar-scanner-cli-3.1.0.1141-linux.zip -d /opt/ && \  
echo 'export PATH=$PATH:/opt/sonar-scanner-3.1.0.1141-linux/bin' >> ~/.bashrc
&& \  
rm sonar-scanner-cli-3.1.0.1141-linux.zip  
  
# Configuro php-fpm  
RUN rm /etc/php/7.0/fpm/pool.d/www.conf  
ADD /etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
# FIX DEI PERMESSI IN SCRITTURA/LETTURA PER L'UTENTE WWW-DATA  
# A volte il gruppo principale per l'utente locale potrebbe essere differente
da 1000  
# (ad esempio un secondo o terzo utente creato), per verificare usate il
comando "id -g"  
RUN usermod -u 1000 www-data  
  
ENTRYPOINT ["/entrypoint.sh"]  

