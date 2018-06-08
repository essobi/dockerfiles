FROM labengine/ubuntu:14.04.5  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
#Added to avoid in container connection to the database with mysql client
error message "TERM environment variable not set"  
ENV TERM dumb  
ENV MARIADB_VERSION 10.1  
ENV MARIADB_PASS root  
ENV MARIADB_USER root  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# to add data on OSX  
RUN usermod -u 1000 mysql  
  
# scripts base to run MariaDB  
COPY scripts/ /root  
RUN chmod 775 /root/*.sh  
  
# Run install packages  
RUN ./root/install_mariadb.sh  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# EXPOSE port  
EXPOSE 3306  
CMD ["/root/start_mariadb.sh"]  

