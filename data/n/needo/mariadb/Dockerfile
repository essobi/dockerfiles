FROM phusion/baseimage:0.9.11  
MAINTAINER needo <needo@superhero.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -q  
  
# Install Dependencies  
RUN apt-get install -qy mariadb-server  
  
# Tweak my.cnf  
RUN sed -i -e 's#\\(bind-address.*=\\).*#\1 0.0.0.0#g' /etc/mysql/my.cnf  
RUN sed -i -e 's#\\(log_error.*=\\).*#\1 /db/mysql_safe.log#g'
/etc/mysql/my.cnf  
RUN sed -i -e 's/\\(user.*=\\).*/\1 nobody/g' /etc/mysql/my.cnf  
  
# InnoDB engine to use 1 file per table, vs everything in ibdata.  
RUN echo '[mysqld]' > /etc/mysql/conf.d/innodb_file_per_table.cnf  
RUN echo 'innodb_file_per_table' >>
/etc/mysql/conf.d/innodb_file_per_table.cnf  
  
EXPOSE 3306  
VOLUME /db  
  
# Add mariadb to runit  
RUN mkdir /etc/service/mariadb  
ADD mariadb.sh /etc/service/mariadb/run  
RUN chmod +x /etc/service/mariadb/run  

