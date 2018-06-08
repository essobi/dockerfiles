FROM debian:8.5  
MAINTAINER El Hadji Samba KANE <elhadjisamba.kane@gmail.com>  
  
# FreeSWITCH  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget \  
subversion \  
ca-certificates  
  
RUN wget -O -
https://files.freeswitch.org/repo/deb/debian/freeswitch_archive_g0.pub | apt-
key add - \  
&& echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.6/ jessie main"
> /etc/apt/sources.list.d/freeswitch.list  
  
RUN apt-get update \  
&& apt-get install -y --fix-missing --force-yes freeswitch-video-deps-most \  
libyuv-dev \  
libvpx2-dev \  
&& git config --global pull.rebase true  
  
WORKDIR /usr/src/  
RUN git clone https://freeswitch.org/stash/scm/fs/freeswitch.git -bv1.6
freeswitch  
WORKDIR freeswitch  
RUN ./bootstrap.sh -j  
COPY modules.conf modules.conf  
RUN ./configure --enable-core-pgsql-support --enable-zrtp \  
&& make \  
&& make install \  
&& make hd-sounds-fr-install \  
&& make hd-moh-install  
  
# Nginx Php-fpm  
RUN apt-get install -y --no-install-recommends nginx \  
php5-fpm \  
supervisor \  
php5-sqlite \  
php-db \  
libpq-dev \  
php5-pgsql \  
php5-mysql \  
php5-common \  
php5-gd \  
php-pear \  
php5-memcache \  
php-apc \  
php5-json \  
ssl-cert \  
git  
  
### Supervisor Fail2ban monit  
RUN apt-get install -y --no-install-recommends supervisor \  
fail2ban \  
monit \  
net-tools \  
iptables  
  
# Fusionpbx  
WORKDIR /var/www/  
RUN rm -rf *  
RUN git clone https://github.com/fusionpbx/fusionpbx fusionpbx  
  
### Nettoyage  
RUN apt-get autoremove -y --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

