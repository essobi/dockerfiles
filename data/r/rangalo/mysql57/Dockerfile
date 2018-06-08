FROM rangalo/ubuntu:latest  
  
MAINTAINER rangalo "hard.mehta@gmail.com"  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && \  
apt-get install -y mysql-server-5.7 && \  
rm -rf /var/lib/apt/lists/*  
  
# remove pre-install database  
RUN rm -rf /var/lib/mysql/*  
  
ADD mysqld-charset.cnf /etc/mysql/conf.d/mysqld-charset.cnf  
ADD mysqld-skip-name-resolv.cnf /etc/mysql/conf.d/mysqld-skip-name-resolv.cnf  
  
ADD configureMysql.sh /configureMysql.sh  
RUN chmod 755 /*.sh  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/configureMysql.sh"]  

