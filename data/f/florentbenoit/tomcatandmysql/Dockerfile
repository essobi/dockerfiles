FROM codenvy/jdk7_tomcat7  
  
# Disable frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install MYSQL  
RUN sudo apt-get update && \  
sudo apt-get install pwgen && \  
sudo -E bash -c "apt-get -y --no-install-recommends install mysql-server" && \  
sudo sed -i.bak 's/127.0.0.1/0.0.0.0/g' /etc/mysql/my.cnf && \  
sudo service mysql restart && \  
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'; FLUSH
PRIVILEGES;"  
  
# Create MySQL user and database  
RUN sudo service mysql restart && \  
CODENVY_MYSQL_PASSWORD=password && \  
CODENVY_MYSQL_DB=petclinic && \  
CODENVY_MYSQL_USER=petclinic && \  
echo "MySQL password: $CODENVY_MYSQL_PASSWORD" >> /home/user/.mysqlrc && \  
echo "MySQL user : $CODENVY_MYSQL_USER" >> /home/user/.mysqlrc && \  
echo "MySQL Database:$CODENVY_MYSQL_DB" >> /home/user/.mysqlrc && \  
sudo mysql -uroot -e "CREATE USER '$CODENVY_MYSQL_USER'@'%' IDENTIFIED BY
'"$CODENVY_MYSQL_PASSWORD"'" && \  
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO '$CODENVY_MYSQL_USER'@'%'
IDENTIFIED BY '"$CODENVY_MYSQL_PASSWORD"'; FLUSH PRIVILEGES;" && \  
sudo mysql -uroot -e "CREATE DATABASE $CODENVY_MYSQL_DB;"  
  
# expose MYSQL port  
EXPOSE 3306  
# Set JVM options (low memory)  
ENV JAVA_OPTS -Djava.awt.headless=true -server -Xms48m -Xmx200M
-XX:MaxPermSize=200m  

