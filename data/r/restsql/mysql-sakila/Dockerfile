# Contains sakila database  
FROM ubuntu:latest  
  
MAINTAINER Mark Sawers <mark.sawers@restsql.org>  
  
# Include our scripts  
ADD ./scripts /etc/mysql/sakila  
  
# Tell debconf to use the noninteractive frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Tell debconf that the default MySQL root password should be "sakila"  
RUN echo 'mysql-server mysql-server/root_password password sakila' | debconf-
set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password sakila' |
debconf-set-selections  
  
# Install MySQL  
RUN apt-get update && apt-get -y install mysql-server  
  
# Start MySQL and run our scripts  
WORKDIR /etc/mysql/sakila  
RUN service mysql restart \  
&& mysql --user=root --password=sakila < init-root.sql \  
&& mysql --user=root --password=sakila < sakila-schema.sql \  
&& mysql --user=root --password=sakila < sakila-data.sql \  
&& mysql --user=root --password=sakila < sakila-schema-ext.sql \  
&& mysql --user=root --password=sakila < sakila-data-ext.sql  
  
EXPOSE 3306  
ENTRYPOINT mysqld_safe --bind-address=0.0.0.0  

