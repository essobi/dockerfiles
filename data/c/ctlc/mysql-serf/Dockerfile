FROM ubuntu:quantal  
MAINTAINER Lucas Carlson <lucas@rufy.com>  
  
# Install packages  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN ! DEBIAN_FRONTEND=noninteractive apt-get -qy install supervisor unzip
mysql-server pwgen; ls  
  
ADD https://dl.bintray.com/mitchellh/serf/0.5.0_linux_amd64.zip serf.zip  
RUN unzip serf.zip  
RUN rm serf.zip  
RUN mv serf /usr/bin/  
  
# Add image configuration and scripts  
ADD /start.sh /start.sh  
ADD /start-serf.sh /start-serf.sh  
ADD /serf-join.sh /serf-join.sh  
ADD /run.sh /run.sh  
ADD /supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
ADD /supervisord-serf.conf /etc/supervisor/conf.d/supervisord-serf.conf  
ADD /my.cnf /etc/mysql/conf.d/my.cnf  
ADD /create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD /import_sql.sh /import_sql.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 3306  
CMD ["/run.sh"]  

