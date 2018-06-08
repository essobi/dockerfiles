FROM monami0ya/docker-baseimage:14.04  
MAINTAINER Masaki Muranaka <monaka@monami-ya.jp>  
  
ENV DEBIAN_FRONTENTD=noninteractive  
ENV LC_ALL=en_US.UTF8  
  
VOLUME /data  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
apt-get -q -y update && \  
apt-get -q -y install software-properties-common unzip && \  
apt-key adv --recv-keys \--keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb http://ftp.cc.uoc.gr/mirrors/mariadb/repo/10.0/ubuntu
trusty main' && \  
apt-get -q -y update && \  
echo mariadb-galera-server-10.0 mysql-server/root_password password root |
debconf-set-selections && \  
echo mariadb-galera-server-10.0 mysql-server/root_password_again password root
| debconf-set-selections && \  
apt-get -o Dpkg::Options::='--force-confnew' -qqy install mariadb-galera-
server galera mariadb-client && \  
apt-get -q -y autoremove && \  
apt-get -q -y clean && \  
service mysql stop && \  
mkdir /etc/service/mariadb  
  
ADD start /etc/service/mariadb/run  
  
CMD ["/sbin/my_init"]  

