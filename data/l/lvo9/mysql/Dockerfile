FROM ubuntu:trusty  
MAINTAINER Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>  
  
# Add MySQL configuration  
COPY my.cnf /etc/mysql/conf.d/my.cnf  
COPY mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
RUN apt-get update && \  
apt-get -yq install mysql-server-5.6 pwgen && \  
rm -rf /var/lib/apt/lists/* && \  
rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf && \  
if [ ! -f /usr/share/mysql/my-default.cnf ] ; then cp /etc/mysql/my.cnf
/usr/share/mysql/my-default.cnf; fi && \  
mysql_install_db > /dev/null 2>&1 && \  
touch /var/lib/mysql/.EMPTY_DB  
  
# Add MySQL scripts  
COPY import_sql.sh /import_sql.sh  
COPY run.sh /run.sh  
  
ENV MYSQL_USER=admin \  
MYSQL_PASS=**Random** \  
ON_CREATE_DB=**False** \  
REPLICATION_MASTER=**False** \  
REPLICATION_SLAVE=**False** \  
REPLICATION_USER=replica \  
REPLICATION_PASS=replica  
  
# Volume for initialization et replication flags  
RUN mkdir /flags  
  
# Keep environment variables with sudo  
RUN echo "Defaults env_keep += \"MYSQL_USER\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"MYSQL_PASS\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"ON_CREATE_DB\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"REPLICATION_MASTER\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"REPLICATION_SLAVE\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"REPLICATION_USER\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"REPLICATION_PASS\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"EXTRA_OPTS\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"RANDOM\"" >>/etc/sudoers  
RUN echo "Defaults env_keep += \"STARTUP_SQL\"" >>/etc/sudoers  
  
# Use user without root privileges  
RUN adduser --disabled-password --gecos "" user1  
RUN echo "user1 ALL = (root) NOPASSWD: /run.sh" >> /etc/sudoers  
RUN echo "user1 ALL = (root) NOPASSWD: /import_sql.sh" >> /etc/sudoers  
USER user1  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/flags"]  
  
EXPOSE 3306  
CMD ["sudo", "/run.sh"]  

