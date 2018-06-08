FROM repositoryjp/centos:6.7  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="MySQL 5.6.29 Server Image" \  
description="The image for creating docker container of MySQL 5.6.29 Server."
\  
distribution="centos" \  
centos-version="6.7" \  
mysql-version="5.6.29" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
ENV MYSQL_VERSION 5.6.29  
USER root  
WORKDIR /tmp  
  
# Create mysql user.  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# Install necessary packages.  
RUN yum install -y libtool \  
libaio \  
libaio-devel \  
zlib-devel \  
numactl  
  
# Install MySQL.  
RUN wget https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-
client-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
rpm -U MySQL-client-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
wget https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-
server-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
rpm -U MySQL-server-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
wget https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-
devel-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
rpm -U MySQL-devel-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
wget https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-shared-
compat-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
rpm -U MySQL-shared-compat-${MYSQL_VERSION}-1.el6.x86_64.rpm && \  
wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-
python-2.1.3-1.el6.x86_64.rpm && \  
rpm -U mysql-connector-python-2.1.3-1.el6.x86_64.rpm && \  
wget https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-
utilities-1.5.6-1.el6.noarch.rpm && \  
rpm -U mysql-utilities-1.5.6-1.el6.noarch.rpm && \  
rm -rf  
  
COPY etc/my.cnf /etc/my.cnf  
RUN chmod 644 /etc/my.cnf  
  
# Configure container.  
USER root  
WORKDIR /root  
  
EXPOSE 3306  
VOLUME /var/lib/mysql  
  
CMD ["/usr/bin/mysqld_safe"]  

