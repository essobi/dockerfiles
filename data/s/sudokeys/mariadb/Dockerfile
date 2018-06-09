FROM sudokeys/baseimage  
MAINTAINER Bertrand RETIF <bertrand@sudokeys.com>  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Install MariaDB from repository.  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0xcbcb082a1bb943db && \  
echo "deb http://ftp.osuosl.org/pub/mariadb/repo/10.0/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/mariadb.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes mariadb-server  
  
# Install other tools.  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y pwgen inotify-tools  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure the database to use our data dir.  
RUN sed -i -e 's/^datadir\s*=.*/datadir = \/data/' /etc/mysql/my.cnf  
  
# Configure MariaDB to listen on any address.  
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf  
  
# Change the innodb-buffer-pool-size to 128M (default is 256M).  
# This should make it friendlier to run on low memory servers.  
#RUN sed -i -e 's/^innodb_buffer_pool_size\s*=.*/innodb_buffer_pool_size =
128M/' /etc/mysql/my.cnf  
EXPOSE 3306  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
RUN touch /firstrun  
  
# Expose our data, log, and configuration directories.  
VOLUME ["/data", "/var/log/mysql", "/etc/mysql"]  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init", "--", "/scripts/start.sh"]  

