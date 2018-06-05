#MariaDB (https://mariadb.org/)  
FROM ubuntu:14.10  
MAINTAINER Boggart <github.com/Boggart>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install MariaDB from repository.  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository -y 'deb http://mariadb.mirror.iweb.com//repo/10.0/ubuntu
utopic main' && \  
apt-get update && \  
apt-get install -y mariadb-server  
  
#disable syslog  
RUN rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf  
  
# Install other tools.  
RUN apt-get install -y pwgen inotify-tools  
  
# Configure the database to use our data dir.  
RUN sed -i -e 's/^datadir\s*=.*/datadir = \/data/' /etc/mysql/my.cnf  
  
# Configure MariaDB to listen on any address.  
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf  
  
# Change the innodb-buffer-pool-size to 128M (default is 256M).  
# This should make it friendlier to run on low memory servers.  
RUN sed -i -e 's/^innodb_buffer_pool_size\s*=.*/innodb_buffer_pool_size =
128M/' /etc/mysql/my.cnf  
  
EXPOSE 3306  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
RUN touch /firstrun  
  
# Expose our data, log, and configuration directories.  
VOLUME ["/data", "/var/log/mysql", "/etc/mysql"]  
  
CMD ["/scripts/start.sh"]  

