FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y curl  
  
# Include our scripts  
RUN /usr/bin/curl -sSL -O http://pentaho.dlpage.phi-
integration.com/mondrian/mysql-foodmart-database/foodmart_mysql.tar.gz \  
&& tar -xzf foodmart_mysql.tar.gz \  
&& rm -f foodmart_mysql.tar.gz  
  
# Tell debconf to use the noninteractive frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Tell debconf that the default MySQL root password should be "foodmart"  
RUN echo 'mysql-server mysql-server/root_password password foodmart' |
debconf-set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password foodmart' |
debconf-set-selections  
  
# Install MySQL  
RUN apt-get update && apt-get -y install mysql-server  
  
# Start MySQL and run our scripts  
RUN service mysql restart \  
&& echo "create database foodmart" | mysql --user=root --password=foodmart \  
&& mysql --user=root --password=foodmart foodmart < foodmart_mysql.sql \  
&& echo "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'foodmart'
WITH GRANT OPTION;" | mysql --user=root --password=foodmart  
  
EXPOSE 3306  
ENTRYPOINT mysqld_safe --bind-address=0.0.0.0

