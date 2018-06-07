FROM ubuntu:latest  
  
MAINTAINER Joshua Brooks "josh.vdbroek@gmail.com"  
ENV DEBIAN_FRONTEND=noninteractive  
  
# ADD ./apt.conf /etc/apt/apt.conf  
RUN apt-get update && apt-get install -y mariadb-server mariadb-client && apt-
get clean  
  
ADD ./run-db.sh /run-db.sh  
RUN chmod +x /run-db.sh  
  
RUN mysql_install_db  
RUN service mysql start && \  
'/usr/bin/mysqladmin' -u root password 'secret' && \  
mysql -uroot -psecret -e \  
"GRANT ALL PRIVILEGES ON *.* TO 'xgcc'@'%' IDENTIFIED BY 'secret';\  
GRANT ALL ON *.* TO 'xgcc'@'%' IDENTIFIED BY 'secret';\  
GRANT GRANT OPTION ON *.* TO 'xgcc'@'%' IDENTIFIED BY 'secret';\  
FLUSH PRIVILEGES;"  
RUN sed -i -e's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf  
EXPOSE 3306  
ENTRYPOINT ["/run-db.sh"]  

