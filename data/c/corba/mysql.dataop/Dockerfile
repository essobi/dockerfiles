FROM ubuntu:16.04  
MAINTAINER Cornel  
  
  
COPY sql-scripts/dataop.init.sql /dataop.init.sql  
COPY mysql-config/my.cnf /etc/mysql/my.cnf  
  
# install mysql  
RUN apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
RUN /usr/bin/mysqld_safe & \  
sleep 10s \  
&& mysql -uroot < /dataop.init.sql \  
&& mysql -uroot -e "UPDATE mysql.user SET
authentication_string=PASSWORD('azure') WHERE User='root'; FLUSH PRIVILEGES;"
\  
&& rm /dataop.init.sql  
  
# copy some scripts to run MySql  
COPY scripts/start-mysql.sh /start-mysql.sh  
  
CMD ["/start-mysql.sh"]  
#ENTRYPOINT ["/usr/bin/mysqld_safe"]  

