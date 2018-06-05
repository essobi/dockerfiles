FROM ubuntu:14.04  
MAINTAINER avadhutp  
  
LABEL description="To test out anemometer+mysql monitoring; especially, slow
query log."  
  
# Install basic dependencies  
RUN \  
apt-get install -y git && \  
apt-get install -y apache2 php5 php5-cli libapache2-mod-php5 php5-gd php5-json
php5-mysql  
  
# Install MySQL  
RUN \  
apt-get update && \  
apt-get install -y mysql-server && \  
apt-get install -y mysql-client  
  
# Install percona-toolkit  
RUN \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \  
echo "deb http://repo.percona.com/apt `lsb_release -cs` main" >
/etc/apt/sources.list.d/percona.list && \  
apt-get update && \  
apt-get install -y percona-toolkit  
  
# Install anemometer  
RUN \  
cd /var/www/html && \  
git clone git://github.com/box/Anemometer.git anemometer && \  
cd anemometer && \  
service mysql start && \  
mysql < install.sql  
  
# Install anemometer config with the correct db connection  
COPY dockerfiles/ibex/conf/config.inc.php
/var/www/html/anemometer/conf/config.inc.php  
  
# Move apache to port 8888  
RUN sed -i 's/Listen 80/Listen 8888/g' /etc/apache2/ports.conf && \  
rm /etc/apache2/sites-enabled/000-default.conf  
COPY dockerfiles/ibex/conf/anemometer-virtualhost.conf /etc/apache2/sites-
enabled/000-anemometer.conf  
  
# Start stuff  
CMD \  
service mysql start && \  
apachectl -D FOREGROUND  
  
EXPOSE 8888  

