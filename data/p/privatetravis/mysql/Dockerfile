FROM privatetravis/base  
MAINTAINER nick_schuch  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MYSQL_USER root  
ENV MYSQL_PASS root  
  
RUN apt-get update  
  
##  
# Configuration.  
##  
RUN echo "mysql-server mysql-server/root_password password $MYSQL_USER" |
debconf-set-selections  
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PASS"
| debconf-set-selections  
  
##  
# Packages.  
##  
RUN apt-get install -y mysql-server  
  
# We do this so all other Docker containers can access this host.  
RUN sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf  
ADD scripts/configure_mysql.sh /root/configure_mysql.sh  
RUN chmod 775 /root/configure_mysql.sh  
RUN sh /root/configure_mysql.sh  
  
##  
# Run tests.  
##  
ADD Rakefile Rakefile  
COPY spec spec  
RUN rake spec  
  
EXPOSE 3306  
CMD [ "mysqld_safe" ]  

