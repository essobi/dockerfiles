FROM marcelesser/ubuntu:trusty  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get install -y software-properties-common \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 4F4EA0AAE5267A6C \  
&& add-apt-repository -y ppa:ondrej/apache2 \  
&& add-apt-repository -y ppa:ondrej/php5-5.6 \  
&& apt-get update  
  
RUN apt-get install -y libapache2-mod-php5 \  
apache2 \  
apache2-utils \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-json \  
php5-ldap \  
php5-readline \  
php5-snmp \  
php5-sqlite \  
php5-tidy \  
php5-xmlrpc \  
php5-apcu \  
php5-gearman \  
php5-geoip \  
php5-imagick \  
php5-intl \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-mongo \  
php5-mysqlnd \  
php5-oauth \  
php-db \  
&& apt-get clean  
  
ENTRYPOINT rm -f /var/run/apache2/apache2.pid && /usr/sbin/apache2ctl
-DFOREGROUND  
  
  

