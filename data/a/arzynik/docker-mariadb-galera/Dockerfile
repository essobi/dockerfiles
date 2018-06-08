# MariaDB Galera 10.0/Ubuntu 14.04 64bit  
FROM ubuntu:14.04  
MAINTAINER Devin Smith <devin@crunchbutton.com>  
  
# add the universe repo  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
  
# update apt  
RUN apt-get -q -y update  
  
# install software-properties-common for key management  
RUN apt-get -q -y install software-properties-common wget unzip curl  
  
# add the key for Mariadb Ubuntu repos  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
  
# add the MariaDB repository for 10.0  
RUN add-apt-repository 'deb [arch=amd64,i386]
http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu trusty main'  
  
# alternative versions  
# RUN add-apt-repository 'deb [arch=amd64,i386]
http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu trusty main'  
# RUN add-apt-repository 'deb [arch=amd64,i386]
http://sfo1.mirrors.digitalocean.com/mariadb/repo/5.5/ubuntu trusty main'  
# update apt again  
RUN apt-get -q -y update  
  
# configure the default root password during installation  
RUN echo mariadb-galera-server-5.5 mysql-server/root_password password root |
debconf-set-selections  
  
# confirm the password (as in the usual installation)  
RUN echo mariadb-galera-server-5.5 mysql-server/root_password_again password
root | debconf-set-selections  
  
# install the necessary packages  
RUN LC_ALL=en_US.utf8 DEBIAN_FRONTEND=noninteractive apt-get -o
Dpkg::Options::='--force-confnew' -qqy install rsync galera mariadb-galera-
server mariadb-client  
  
# 10.1 uses no longer uses the mariadb-galera-server package  
# RUN LC_ALL=en_US.utf8 DEBIAN_FRONTEND=noninteractive apt-get -o
Dpkg::Options::='--force-confnew' -qqy install rsync galera mariadb-server
mariadb-client  
# upload the locally created my.cnf  
ADD ./my.cnf /etc/mysql/my.cnf  
  
# startup the service - this will fail since the nodes haven't been configured
on first boot  
RUN service mysql restart  
  
RUN mkdir -p /data  
  
# open the ports required to connect to MySQL and for Galera SST / IST
operations  
EXPOSE 3306 4444 4567 4568  
ADD start /bin/start  
RUN chmod +x /bin/start  

