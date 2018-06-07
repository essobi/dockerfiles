FROM bmoorman/ubuntu:bionic  
  
ENV HTTPD_SERVERNAME="localhost"  
ARG DEBIAN_FRONTEND="noninteractive"  
RUN echo 'deb http://ppa.launchpad.net/certbot/certbot/ubuntu bionic main' >
/etc/apt/sources.list.d/certbot.list \  
&& echo 'deb-src http://ppa.launchpad.net/certbot/certbot/ubuntu bionic main'
>> /etc/apt/sources.list.d/certbot.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 75BCA694 \  
&& apt-get update \  
&& apt-get install --yes --no-install-recommends \  
apache2 \  
certbot \  
curl \  
libapache2-mod-php \  
php-sqlite3 \  
ssl-cert \  
&& a2enmod \  
remoteip \  
rewrite \  
ssl \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY apache2/ /etc/apache2/  
COPY htdocs/ /var/www/html/  
  
VOLUME /config  
  
EXPOSE 7539  
CMD ["/etc/apache2/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:80/ > /dev/null || exit 1  

