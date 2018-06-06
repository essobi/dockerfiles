FROM bmoorman/ubuntu:xenial  
  
ENV HTTPD_SERVERNAME="localhost"  
ARG DEBIAN_FRONTEND="noninteractive"  
WORKDIR /var/www  
  
RUN echo 'deb http://ppa.launchpad.net/certbot/certbot/ubuntu xenial main' >
/etc/apt/sources.list.d/certbot.list \  
&& echo 'deb-src http://ppa.launchpad.net/certbot/certbot/ubuntu xenial main'
>> /etc/apt/sources.list.d/certbot.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 75BCA694 \  
&& apt-get update \  
&& apt-get install --yes --no-install-recommends \  
apache2 \  
certbot \  
curl \  
git \  
libapache2-mod-php \  
php-curl \  
php-sqlite3 \  
php-xml \  
php-zip \  
ssl-cert \  
&& a2enmod \  
remoteip \  
rewrite \  
ssl \  
&& git clone https://github.com/causefx/Organizr \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY apache2/ /etc/apache2/  
  
VOLUME /config  
  
EXPOSE 9357  
CMD ["/etc/apache2/start.sh"]  
  
HEALTHCHECK \--interval=60s --timeout=5s CMD curl --silent --location --fail
http://localhost:80/ > /dev/null || exit 1  

