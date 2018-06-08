FROM ubuntu:trusty  
MAINTAINER Adrien de Pierres <adrien@arccoza.com>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
echo 'deb http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu trusty
main' >> /etc/apt/sources.list && \  
echo 'deb-src http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu
trusty main' >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y mariadb-server pwgen && \  
rm -rf /var/lib/mysql/* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV INNODB_BUFFER_POOL_SIZE 128M  
  
ADD mysql_config_users.sh /mysql_config_users.sh  
ADD run.sh /run.sh  
RUN chmod 775 /*.sh  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
#Added to avoid in container connection to the database with mysql client
error message "TERM environment variable not set"  
ENV TERM dumb  
  
EXPOSE 3306  
CMD ["/run.sh"]

