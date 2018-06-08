# Full PHP5 stack:  
# * PHP5  
# * Nginx  
# * MariaDB  
# * Postfix  
FROM ubuntu:precise  
MAINTAINER Ryan Seto <ryanseto@yak.net>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade  
  
# Ensure UTF-8  
RUN apt-get update  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install MariaDB from repository.  
# Install PHP5, Nginx, and postfix.  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get -y install python-software-properties && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu
precise main' && \  
apt-get update && \  
apt-get install -y \  
openssh-server \  
mariadb-server \  
nginx \  
postfix \  
supervisor \  
php5-fpm php5-mysql php-apc php5-imagick php5-imap php5-mcrypt php5-gd
libssh2-php \  
rsyslog && \  
/etc/init.d/mysql stop  
  
# Configure Postfix  
run postconf -e mydestination="localhost.localdomain, localhost"  
  
# Ensure required directories exist for sshd and supervisor  
RUN mkdir -p /var/run/sshd && \  
mkdir -p /var/log/supervisor  
  
# Set the root password to "Ahdooch3" (courtesy of pwgen).  
# This feels like a bad idea, but I can't think of a better solution at the
moment.  
RUN echo "root:Ahdooch3" | chpasswd  
  
# Decouple our data from our container.  
VOLUME ["/data"]  
  
# Configure the database to use our data dir.  
RUN sed -i -e 's/^datadir\s*=.*/datadir = \/data/' /etc/mysql/my.cnf  
  
# Allow anyone to write to /tmp. MariaDB depends on this.  
RUN chmod a+w /tmp  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD nginx-site.conf /etc/nginx/sites-available/default  
ADD https://github.com/h5bp/server-configs-nginx/archive/master.tar.gz
/tmp/server-configs-nginx-master.tar.gz  
RUN tar -xzf /tmp/server-configs-nginx-master.tar.gz && \  
cp -R server-configs-nginx-master/h5bp /etc/nginx && \  
rm -rf server-configs-nginx-master && \  
rm /tmp/server-configs-nginx-master.tar.gz  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini && \  
sed -i -e 's/^;daemonize\s*=\s*yes/daemonize = no/' /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e '/access_log/d' /etc/nginx/h5bp/location/expires.conf && \  
sed -i -e 's/^listen =.*/listen = \/var\/run\/php5-fpm.sock/'
/etc/php5/fpm/pool.d/www.conf  
  
# Add the supervisord configuration.  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Decouple our data from our container.  
VOLUME ["/srv/www"]  
  
EXPOSE 22 80  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ENTRYPOINT ["/start.sh"]  

