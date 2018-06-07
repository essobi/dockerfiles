#  
# Kuali Coeus on MySQL Server Dockerfile  
#  
# https://github.com/jefferyb/docker-mysql-kuali-coeus  
#  
# To Build:  
# docker build -t jefferyb/kuali_db_mysql .  
#  
# To Run:  
# docker run -d --name kuali_database -h kuali_database -p 3306:3306
jefferyb/kuali_db_mysql  
#  
# Pull base image.  
FROM ubuntu:16.04  
MAINTAINER Jeffery Bagirimvano <jeffery.rukundo@gmail.com>  
  
RUN mkdir -p /setup_files  
ADD setup_files /setup_files  
  
ENV HOST_NAME kuali_database  
  
ENV MYSQL_ROOT_PASSWORD="Chang3m3t0an0th3r"  
ENV MYSQL_DATABASE="kualicoeusdb"  
ENV MYSQL_USER="kcusername"  
ENV MYSQL_PASSWORD="kcpassword"  
# Install MySQL.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server git && \  
rm -rf /var/lib/apt/lists/* && \  
###  
echo $(head -1 /etc/hosts | cut -f1) ${HOST_NAME} >> /etc/hosts && \  
echo "mysqld_safe &" > /tmp/config && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"localhost\" WITH
GRANT OPTION;'" >> /tmp/config && \  
bash /tmp/config && \  
rm -f /tmp/config && \  
### Set root password  
mysqladmin -u root password ${MYSQL_ROOT_PASSWORD} && \  
mysqladmin -u root -p${MYSQL_ROOT_PASSWORD} -h ${HOST_NAME} password
${MYSQL_ROOT_PASSWORD} && \  
### For Kuali Coeus  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/mysql.conf.d/mysqld.cnf &&
\  
echo "transaction-isolation = READ-COMMITTED" >>
/etc/mysql/mysql.conf.d/mysqld.cnf && \  
echo "lower_case_table_names = 1" >> /etc/mysql/mysql.conf.d/mysqld.cnf && \  
echo
"sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
>> /etc/mysql/mysql.conf.d/mysqld.cnf && \  
### Create user & database  
mysql -u root -p${MYSQL_ROOT_PASSWORD} -e " \  
CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE CHARACTER SET utf8 COLLATE
utf8_bin; \  
GRANT ALL ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}'@'%' IDENTIFIED BY
'${MYSQL_PASSWORD}'; \  
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE
TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, CREATE ROUTINE, ALTER ROUTINE ON *
. * TO '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}' WITH
MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0
MAX_USER_CONNECTIONS 0 ; \  
"; \  
service mysql restart && \  
###  
cd /setup_files; ./install_kuali_db.sh && \  
rm -fr /setup_files && \  
echo "Done!!!"  
# Expose ports.  
EXPOSE 3306  
# Define default command.  
CMD /usr/bin/mysqld_safe  

