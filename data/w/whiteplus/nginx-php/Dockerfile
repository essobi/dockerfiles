FROM debian:jessie  
  
MAINTAINER WHITEPLUS System "sysadmin@wh-plus.com"  
  
ENV NGINX_VERSION 1.9.5-1~jessie  
  
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list
\  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 \--recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 \--recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4 \  
&& echo "deb http://packages.elastic.co/beats/apt stable main" | tee -a
/etc/apt/sources.list.d/beats.list \  
&& apt-get update 1> /dev/null \  
&& apt-get upgrade -y -q --no-install-recommends \  
&& apt-get install -y \--no-install-recommends \  
libcurl4-openssl-dev \  
ca-certificates nginx=${NGINX_VERSION} supervisor \  
php5-fpm php5-mysql php-apc php5-curl php5-gd php5-intl php5-mcrypt
php5-memcache \  
php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo
libapache2-mod-php5 \  
php5-xdebug \  
packetbeat \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

