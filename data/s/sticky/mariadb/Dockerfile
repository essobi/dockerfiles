# MariaDB (https://mariadb.org/)  
FROM ubuntu:precise  
MAINTAINER Laurens Duijvesteijn <l.duijvesteijn@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# Install MariaDB from repository.  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get -y install python-software-properties && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu
precise main' && \  
apt-get update && \  
apt-get install -y mariadb-server  
  
# Install other tools.  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y pwgen inotify-tools  
  
# Configure the database to use our data dir.  
RUN sed -i -e 's/^datadir\s*=.*/datadir = \/var\/lib\/mysql/'
/etc/mysql/my.cnf  
  
# Configure MariaDB to listen on any address.  
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf  
  
EXPOSE 3306  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
RUN touch /firstrun  
  
ENTRYPOINT ["/scripts/start.sh"]  

