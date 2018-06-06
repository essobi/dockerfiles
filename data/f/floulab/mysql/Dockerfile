FROM mysql:5.7  
  
MAINTAINER Ioannis Angelakopoulos<ioagel@gmail.com>  
  
ENV UID=112 GID=116  
  
RUN groupmod -g $GID mysql && \  
usermod -u $UID mysql && \  
chown -R mysql:mysql /var/lib/mysql \  
/var/run/mysqld \  
/var/lib/mysql-files \  
/var/lib/mysql-keyring && \  
chown -R mysql /var/log/mysql  

