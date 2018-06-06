FROM column/base:v1  
  
MAINTAINER Column Fang <column.fang@gmail.com>  
  
COPY files /  
  
RUN \  
# Install MySQL 5.7  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.7 && \  
mkdir -p /var/run/mysqld && \  
chown mysql:mysql /var/run/mysqld && \  
  
# Configure for MySQL  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/mysql.conf.d/mysqld.cnf &&
\  
  
# Clean preinstalled data  
rm -rf /var/lib/mysql/* && \  
# Cleanup  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/lib/mysql  
EXPOSE 3306  

