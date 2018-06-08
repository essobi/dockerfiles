FROM debian:jessie  
MAINTAINER Stéphane Cottin <stephane.cottin@vixns.com>  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
echo 'deb http://ftp.igh.cnrs.fr/pub/mariadb/repo/10.2/debian jessie main' >>
/etc/apt/sources.list && \  
apt-get update && apt-get -y dist-upgrade && \  
apt-get install --no-install-recommends --no-install-suggests --auto-remove -y
mariadb-server galera-3 mariadb-client xtrabackup netcat socat procps host
socat unzip rsync && \  
rm -rf /var/lib/apt/lists/*  
  
# install galera-healthcheck  
ADD https://github.com/vixns/galera-
healthcheck/releases/download/v20160702/galera-healthcheck_linux_amd64
/bin/galera-healthcheck  
RUN test "$(sha256sum /bin/galera-healthcheck | awk '{print $1;}')" =
"74cafdeda7a87abbf5e7667b1ad8ce3eecefddf09bdc5aa38a8e9661f15c8f31"  
RUN chmod +x /bin/galera-healthcheck  
  
# configure mysqld  
RUN sed -i 's/#? *bind-address/# bind-address/' /etc/mysql/my.cnf  
RUN sed -i 's/#? *log-error/# log-error/' /etc/mysql/my.cnf  
ADD conf.d/utf8.cnf /etc/mysql/conf.d/utf8.cnf  
ADD conf.d/galera.cnf /etc/mysql/conf.d/galera.cnf  
RUN chmod 0644 /etc/mysql/conf.d/utf8.cnf  
RUN chmod 0644 /etc/mysql/conf.d/galera.cnf  
  
EXPOSE 3306 4444 4567 4568  
VOLUME ["/var/lib/mysql"]  
COPY start /start  
COPY mysqld.sh /mysqld.sh  
RUN chmod 555 /start /mysqld.sh  
ENTRYPOINT ["/start"]  

