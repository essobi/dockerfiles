FROM ubuntu:14.04  
MAINTAINER OEMS <oscaremu@gmail.com>  
  
# On 161104 the current release of cacti on ubuntu 14.04 is 0.8.8b  
ENV CACTI_VERSION 0.8.8b  
ENV JOB "*/5 * * * * php /var/www/html/cacti/poller.php"  
RUN set -x \  
&& apt-get update && apt-get install -y supervisor apache2 mysql-server
rrdtool curl \  
apache2-bin apache2-data dbconfig-common fontconfig fontconfig-config fonts-
dejavu fonts-dejavu-core fonts-dejavu-extra \  
javascript-common libaio1 libapache2-mod-php5 libapr1 libaprutil1
libaprutil1-dbd-sqlite3 libaprutil1-ldap libasn1-8-heimdal libcairo2 \  
libdatrie1 libdbd-mysql-perl libdbi-perl libdbi1 libedit2 libfontconfig1
libfreetype6 libglib2.0-0 libglib2.0-data libgraphite2-3 libgssapi3-heimdal \  
libharfbuzz0b libhcrypto4-heimdal libheimbase1-heimdal libheimntlm0-heimdal
libhtml-template-perl libhx509-5-heimdal libjs-jquery libjs-jquery-cookie \  
libkrb5-26-heimdal libldap-2.4-2 libmysqlclient18 libpango-1.0-0
libpangocairo-1.0-0 libpangoft2-1.0-0 libperl5.18 libphp-adodb libpixman-1-0 \  
libpython-stdlib libpython2.7-minimal libpython2.7-stdlib libroken18-heimdal
librrd4 libsasl2-2 libsasl2-modules libsasl2-modules-db libsensors4 \  
libsnmp-base libsnmp30 libterm-readkey-perl libthai-data libthai0
libwind0-heimdal libwrap0 libx11-6 libx11-data libxau6 libxcb-render0 \  
libxcb-shm0 libxcb1 libxdmcp6 libxext6 libxml2 libxrender1 lsof mysql-
client-5.5 mysql-client-core-5.5 mysql-common \  
mysql-server-5.5 mysql-server-core-5.5 openssl php5-cli php5-common php5-json
php5-mysql php5-readline php5-snmp psmisc python python-meld3 \  
python-minimal python-pkg-resources python2.7 python2.7-minimal sgml-base
shared-mime-info snmp ssl-cert supervisor tcpd ttf-dejavu \  
ttf-dejavu-core ttf-dejavu-extra xml-core \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/www/html/cacti \  
&& cd /var/www/html/cacti \  
&& curl -O "http://www.cacti.net/downloads/cacti-$CACTI_VERSION.tar.gz" \  
&& tar xzf "cacti-$CACTI_VERSION.tar.gz" \--strip 1 \  
&& rm "cacti-$CACTI_VERSION.tar.gz"  
  
RUN service mysql start & \  
sleep 10s \  
&& echo "create database cacti;" | mysql -u root \  
&& echo "GRANT ALL ON cacti.* TO cactiuser@'%' IDENTIFIED BY 'cactiuser';" |
mysql -u rootmysql -u root \  
&& mysql -u root cacti < /var/www/html/cacti/cacti.sql \  
&& tar -cvf /mysql_basic.tar /var/lib/mysql  
  
RUN (crontab -u root -l; echo "$JOB" ) | crontab -u root -  
  
ADD supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

