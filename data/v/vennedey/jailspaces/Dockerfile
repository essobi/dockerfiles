FROM debian:jessie  
  
MAINTAINER Falco Vennedey "jailspaces@vennedey.net"  
ENV DATADIR /data  
  
# Install packages  
ADD http://nginx.org/keys/nginx_signing.key /tmp/nginx.key  
RUN apt-key add /tmp/nginx.key && rm /tmp/nginx.key  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.fr.debian.org/debian/ jessie main contrib non-free" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
php5-fpm \  
python \  
members \  
wget \  
sudo \  
cron \  
unattended-upgrades \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Base system  
COPY files/apt-unattended-upgrade/ /etc/apt/apt.conf.d/  
COPY files/login.defs /etc/  
  
# TLS certificate management  
RUN mkdir -p $DATADIR /root/init  
RUN useradd -b $DATADIR -s /bin/bash -M cert  
ADD https://raw.githubusercontent.com/68b32/acme-tiny/master/acme_tiny.py
/usr/local/bin  
ADD https://raw.githubusercontent.com/68b32/CertWatch/master/CertWatch
/usr/local/bin/CertWatch  
COPY files/sudo /etc/sudoers.d/cert  
COPY files/certconf /root/init/certconf  
COPY files/etc-CertWatch /etc/CertWatch  
COPY files/cert.cron /root/init/cert.cron  
RUN crontab -u cert /root/init/cert.cron  
  
RUN chown cert:cert /usr/local/bin/acme_tiny.py && \  
chmod 700 /usr/local/bin/acme_tiny.py && \  
chown cert:cert /usr/local/bin/CertWatch && \  
chmod 555 /usr/local/bin/CertWatch && \  
chmod 444 /etc/CertWatch && \  
chown root:root /etc/sudoers.d/* && \  
chmod 440 /etc/sudoers.d/*  
  
# Webspace management  
RUN groupadd webspaceuser  
ADD https://raw.githubusercontent.com/68b32/jailspaces-js/master/js
/usr/local/sbin/  
RUN chown root:cert /usr/local/sbin/js && chmod 550 /usr/local/sbin/js  
COPY files/jailspaces/conf/ /etc/jailspaces/  
COPY files/acme_fallback.conf /etc/nginx/conf.d/  
COPY files/php.ini /etc/php5/fpm/  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY files/docker-init.sh /usr/local/sbin/  
  
VOLUME $DATADIR  
  
EXPOSE 80 443  
CMD /usr/local/sbin/docker-init.sh "$DATADIR"  

