# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Salvador Rodriguez <salvador.rodriguez@utah.edu>  
  
# Install packages  
ENV REFRESHED_AT 2015-03-12  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install mysql-server-5.6 pwgen && \  
rm -rf /var/lib/apt/lists/*  
  
# Add MySQL configuration  
ADD config_mysql.sh /config_mysql.sh  
RUN chmod 755 /config_mysql.sh  
RUN /config_mysql.sh  
RUN rm config_mysql.sh  
ADD my.cnf /etc/mysql/my.cnf  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/umlsmeta"]  
  
EXPOSE 3306  
CMD ["mysqld_safe"]  

