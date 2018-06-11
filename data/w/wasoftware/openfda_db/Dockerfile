FROM ubuntu:trusty  
  
# Install packages  
RUN apt-get update && \  
apt-get -yq install mysql-server-5.6 curl  
  
# Enable remote access (default is localhost only, we change this  
# otherwise our database would not be reachable from outside the container)  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# Install database  
ADD ./openfda_db_init.sql /var/db/openfda_db_init.sql  
  
# Set Standard settings  
ENV user openfda_web  
ENV password welcome123  
ENV url file:/var/db/openfda_db_init.sql  
ENV right WRITE  
  
# Install starting script  
ADD ./start-database.sh /usr/local/bin/start-database.sh  
RUN chmod +x /usr/local/bin/start-database.sh  
  
EXPOSE 3306  
CMD ["/usr/local/bin/start-database.sh"]  

