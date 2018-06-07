FROM ubuntu:trusty  
MAINTAINER Andrzej Skrodzki  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install mysql-server mysql-client pwgen sysbench && \  
rm -rf /var/lib/apt/lists/*  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Remove syslog configuration  
RUN rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf  
  
# Add MySQL configuration  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
# Add MySQL scripts  
ADD run.sh /run.sh  
ADD logs /logs  
RUN chmod 755 /*.sh  
  
# Exposed ENV  
ENV MYSQL_USER admin  
ENV MYSQL_PASS test1234  
ENV ON_CREATE_DB test  
  
EXPOSE 3306  
CMD ["/run.sh"]  

