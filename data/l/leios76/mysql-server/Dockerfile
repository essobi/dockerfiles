# Pull base image.  
FROM ubuntu:14.04  
# Install MySQL.  
RUN \  
sed -ri 's/archive\\.ubuntu\\.com/kr\\.archive\\.ubuntu\\.com/g'
/etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.6 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/etc/mysql/conf.d/docker.cnf /etc/mysql/conf.d/docker.cnf  
COPY files/init.sh /init.sh  
  
RUN \  
cp -Ra /var/lib/mysql /var/lib/mysql.default && \  
cp -Ra /etc/mysql /etc/mysql.default  
  
# Define default command.  
CMD ["/init.sh"]  
  
VOLUME ["/var/run/mysqld"]  
  
# Define working directory.  
WORKDIR /var/lib/mysql  
# Expose ports.  
EXPOSE 3306  

