FROM wnameless/mysql-phpmyadmin:latest  
MAINTAINER Glenn ROLLAND, <glenux@glenux.net>  
RUN apt-get update  
RUN echo "root:docker" | chpasswd  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN /usr/sbin/mysqld & \  
sleep 10s && \  
echo "GRANT ALL ON *.* TO root@'%' with grant option; FLUSH PRIVILEGES; " |
mysql -u root  
  
#ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
#ADD supervisor-ssh.conf /etc/supervisor/conf.d/ssh.conf  
#CMD /usr/bin/supervisord  
EXPOSE 3306  

