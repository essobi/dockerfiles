FROM phusion/baseimage:latest  
MAINTAINER sensei73 <sensei73@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#Add a new user: xbmc  
RUN usermod -u 99 nobody \  
&& usermod -g 100 nobody \  
  
&& apt-get update -q \  
  
# Install Dependencies  
&& apt-get update -q \  
&& apt-get install -qy mariadb-server  
&& apt-get clean  
  
# Tweak my.cnf  
RUN sed -i -e 's#\\(bind-address.*=\\).*#\1 0.0.0.0#g' /etc/mysql/my.cnf \  
&& sed -i -e 's#\\(log_error.*=\\).*#\1 /db/mysql_safe.log#g'
/etc/mysql/my.cnf \  
&& sed -i -e 's/\\(user.*=\\).*/\1 nobody/g' /etc/mysql/my.cnf \  
  
# InnoDB engine to use 1 file per table, vs everything in ibdata.  
&& echo '[mysqld]' > /etc/mysql/conf.d/innodb_file_per_table.cnf \  
&& echo 'innodb_file_per_table' >> /etc/mysql/conf.d/innodb_file_per_table.cnf  
  
EXPOSE 3306  
VOLUME /db  
  
# Add mariadb to runit  
RUN mkdir /etc/service/mariadb  
ADD mariadb.sh /etc/service/mariadb/run  
RUN chmod +x /etc/service/mariadb/run  

