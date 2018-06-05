FROM bitergia/ubuntu-trusty  
  
MAINTAINER David Muriel <dmuriel@bitergia.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MARIADB_VERSION 10.0  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/10.0/ubuntu
trusty main' && \  
{ echo 'Package: *'; echo 'Pin: release o=MariaDB'; echo 'Pin-Priority: 999';
} > /etc/apt/preferences.d/mariadb && \  
apt-get update && \  
apt-get -y install debconf-utils && \  
apt-get -y install mariadb-server && \  
sed -ri 's/^(bind-address|skip-networking)/;\1/' /etc/mysql/my.cnf && \  
apt-get -y remove --purge software-properties-common && \  
apt-get -y autoremove --purge && \  
apt-get clean && \  
find /var/lib/apt/lists -type f -delete && \  
rm -fr /var/lib/mysql/*  
  
### Exposed ports  
# - MariaDB default port  
EXPOSE 3306  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

