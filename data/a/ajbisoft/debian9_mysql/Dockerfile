FROM debian:9  
MAINTAINER Jakub Kwiatkowski <jakub@ajbisoft.pl>  
  
COPY mysql.list /etc/apt/sources.list.d/  
COPY mysql.gpg /etc/apt/trusted.gpg.d/  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -yq
install mysql-server \  
&& sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& apt-get -y --purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* \  
&& mv /var/lib/mysql /var/lib/mysql_orig  
  
VOLUME ["/var/lib/mysql"]  
  
COPY docker-entrypoint.sh /  
EXPOSE 3306  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

