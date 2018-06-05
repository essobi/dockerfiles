# MariaDB (https://mariadb.org/)  
FROM ubuntu:14.04  
MAINTAINER Marius Cobzarenco <marius@reinfer.io>  
  
# Ensure UTF-8  
RUN apt-get update  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install MariaDB from repository.  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb
http://mirror.stshosting.co.uk/mariadb/repo/10.1/ubuntu trusty main' && \  
apt-get update && \  
apt-get install -y mariadb-server pwgen inotify-tools  
  
# Decouple our data from our container.  
VOLUME ["/data"]  
  
# Configure the database to use our data dir.  
RUN sed -i -e 's/^datadir\s*=.*/datadir = \/data/' /etc/mysql/my.cnf  
  
# Configure the database to use UTF8  
RUN sed -i -re 's/(^[\\#])(default-character-set|character[-_]set[-_]server)([
]*=.*)/\2 = utf8/;' /etc/mysql/conf.d/mariadb.cnf  
RUN sed -i -re 's/(^[\\#])(collation[-_]server)([ ]*=.*)/\2 =
utf8_general_ci/;' /etc/mysql/conf.d/mariadb.cnf  
  
# Configure MariaDB to listen on any address.  
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf  
  
EXPOSE 3306  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
RUN touch /firstrun  
  
ENTRYPOINT ["/scripts/start.sh"]  

