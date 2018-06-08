FROM debian:jessie  
  
MAINTAINER Metabool  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
#WORKDIR /usr/src  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/01buildconfig
&& \  
echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/01buildconfig && \  
echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf.d/01buildconfig && \  
echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/01buildconfig && \  
apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install curl \  
imagemagick \  
apache2-mpm-prefork \  
apache2 \  
php5-cli \  
php5-mysql \  
php5-gd \  
php5-mcrypt \  
php5-curl \  
php5-memcache \  
php5-xsl \  
php5-intl \  
php5-xmlrpc \  
php5 \  
php5-sqlite \  
php5-sybase \  
php5-snmp \  
php5-dev \  
php-pear \  
ghostscript \  
libapache2-mod-security2 \  
modsecurity-crs \  
mysql-client \  
lynx  
  
RUN sed -i 's/short_open_tag = Off/short_open_tag = On/g'
/etc/php5/apache2/php.ini && \  
sed -i 's/post_max_size = 8M/post_max_size = 800M/g' /etc/php5/apache2/php.ini
&& \  
sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 200M/g'
/etc/php5/apache2/php.ini && \  
cp /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf && \  
a2enmod headers && \  
a2dismod status && \  
a2enmod remoteip  
RUN sed -i 's/ServerTokens OS/ServerTokens Minimal/g' /etc/apache2/conf-
enabled/security.conf && \  
sed -i 's/ServerSignature On/#ServerSignature On/g' /etc/apache2/conf-
enabled/security.conf && \  
sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On\nInclude
\/usr\/share\/modsecurity-crs\/*.conf\nInclude \/usr\/share\/modsecurity-
crs\/base_rules\/*.conf\nInclude \/usr\/share\/modsecurity-
crs\/optional_rules\/*.conf\nSecServerSignature "webserver"/g'
/etc/modsecurity/modsecurity.conf && \  
sed -i 's/SecResponseBodyAccess On/SecResponseBodyAccess Off/g'
/etc/modsecurity/modsecurity.conf && \  
sed -i 's/#SecDebugLogLevel 3/SecDebugLogLevel 0/g'
/etc/modsecurity/modsecurity.conf && \  
sed -i 's/#SecDebugLog \/opt\/modsecurity\/var\/log\/debug.log/SecDebugLog
\/var\/log\/apache2\/modsec_debug.log/g' /etc/modsecurity/modsecurity.conf &&
\  
sed -i 's/#ServerName www.example.com/#ServerName
www.example.com\nSecRuleRemoveById 960017/g' /etc/apache2/sites-
enabled/000-default.conf && \  
sed -i 's/LogFormat "%v:%p %h/LogFormat "%v:%p %a/g' /etc/apache2/apache2.conf
&& \  
sed -i 's/LogFormat "%h/LogFormat "%a/g' /etc/apache2/apache2.conf && \  
echo "RemoteIPHeader X-Real-IP\nRemoteIPTrustedProxy nginx-apache" >
/etc/apache2/conf-enabled/remoteip.conf  
  
RUN mkdir -p /default_conf/apache2 && \  
mkdir -p /default_conf/modsecurity && \  
mkdir -p /default_conf/php5 && \  
mkdir -p /default_conf/modsecurity/crs_rules && \  
cp -Rpv /etc/modsecurity/* /default_conf/modsecurity/ && \  
cp -Rpv /usr/share/modsecurity-crs/* /default_conf/modsecurity/crs_rules/ && \  
cp -Rpv /etc/apache2/* /default_conf/apache2/ && \  
cp -Rpv /etc/php5/* /default_conf/php5/  
  
ADD adds/start /start  
  
EXPOSE 80  
EXPOSE 443  
  
ENTRYPOINT ["/start"]  
#RUN ["/bin/bash"]  

