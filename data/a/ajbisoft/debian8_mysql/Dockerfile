FROM debian:8  
MAINTAINER Jakub Kwiatkowski <jakub@ajbisoft.pl>  
COPY sources.list /etc/apt/  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -y
install mysql-server \  
&& sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf \  
&& apt-get -y --purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  
COPY docker-entrypoint.sh /  
EXPOSE 3306  
ENTRYPOINT ["/docker-entrypoint.sh"]  

