FROM crashvb/supervisord:latest  
MAINTAINER Richard Davis <crashvb@gmail.com>  
  
# Install packages, download files ...  
ENV MYSQL_DATA=/var/lib/mysql  
RUN APT_ALL_REPOS=1 docker-apt mysql-server && \  
rm --force --recursive ${MYSQL_DATA}/*  
  
# Configure: mysql  
RUN install --directory --group=mysql --mode=0750 --owner=mysql
/var/run/mysqld  
  
# Configure: supervisor  
ADD supervisord.mysql.conf /etc/supervisor/conf.d/mysql.conf  
  
# Configure: entrypoint  
ADD entrypoint.mysql /etc/entrypoint.d/20mysql  
  
EXPOSE 3306/tcp  
  
VOLUME /var/lib/mysql  

