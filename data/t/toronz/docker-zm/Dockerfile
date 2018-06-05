#name of container: docker-zm  
#versison of container: 0.0.1  
FROM phusion/baseimage:0.9.21  
LABEL maintainer Tomas Maggio "tomas@sensaway.co.nz"  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN add-apt-repository ppa:iconnor/zoneminder  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
--no-install-recommends software-properties-common  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
--no-install-recommends mysql-server \  
#mariadb-server \  
php7.0-mysql \  
nano \  
#mariadb-client \  
#nginx \  
#nginx-extras \  
fcgiwrap \  
php7.0-fpm \  
ntp \  
ntpdate \  
htop \  
wget \  
php7.0 \  
php7.0-mysql \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php-pear \  
php-imagick \  
php7.0-imap \  
php7.0-mcrypt \  
php-memcache \  
php7.0-pspell \  
php7.0-recode \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-mbstring \  
php-gettext \  
php-apcu \  
php-gd \  
vim \  
usbutils \  
libvlc-dev \  
libvlccore-dev\  
libapache2-mod-perl2 \  
vlc \  
dialog \  
ffmpeg  
  
# to add mysqld deamon to runiti  
RUN mkdir -p /etc/service/mysqld /var/log/mysqld ; sync  
COPY mysqld.sh /etc/service/mysqld/run  
RUN chmod +x /etc/service/mysqld/run \  
&& chown mysql /var/log/mysqld  
  
# to add apache2 deamon to runit  
RUN mkdir -p /etc/service/apache2 /var/log/apache2 ; sync  
COPY apache2.sh /etc/service/apache2/run  
RUN chmod +x /etc/service/apache2/run \  
&& chown -R www-data /var/log/apache2  
  
# to add zm deamon to runit  
RUN mkdir -p /var/log/zm ; sync  
COPY zm.sh /sbin/zm.sh  
RUN chmod +x /sbin/zm.sh  
  
# to add ntp deamon to runit  
RUN mkdir -p /etc/service/ntp /var/log/ntp ; sync  
COPY ntp.sh /etc/service/ntp/run  
RUN chmod +x /etc/service/ntp/run \  
&& chown -R nobody /var/log/ntp  
  
#startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
#pre-config scritp for different service that need to be run when container
image is create  
#maybe include additional software that need to be installed ... with some
service running ... like example mysqld  
COPY pre-conf.sh /sbin/pre-conf  
RUN chmod +x /sbin/pre-conf ; sync \  
&& /bin/bash -c /sbin/pre-conf \  
&& rm /sbin/pre-conf  
  
##scritp that can be running from the outside using docker-bash tool ...  
## for example to create backup for database with convitation of VOLUME
dockers-bash container_ID backup_mysql  
COPY backup.sh /sbin/backup  
RUN chmod +x /sbin/backup  
VOLUME /var/backups  
  
RUN echo "!/bin/sh ntpdate 0.ubuntu.pool.ntp.org" >> /etc/cron.daily/ntpdate \  
&& chmod 750 /etc/cron.daily/ntpdate  
  
VOLUME /var/lib/mysql /var/cache/zoneminder  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

