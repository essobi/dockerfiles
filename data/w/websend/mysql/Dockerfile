# NAME: MySQL  
#  
# DESCRIPTION: MySQL image.  
#  
# REQUIRED ENVS: DATA_DIRECTORY  
#  
# OPTIONAL ENVS: ROOT_PASSWORD  
#  
# USAGE EXAMPLE: docker run websend/mysql  
FROM websend/debian:7.7  
MAINTAINER Ilja Krijger <i.krijger@websend.nl>  
  
Add files/mysql.list /etc/apt/sources.list.d/mysql.list  
  
RUN \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 5072E1F5 && \  
useradd -m -u 3306 mysql && \  
apt-get update && \  
apt-get install -yq mysql-server && \  
apt-get install -yq inotify-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf /etc/mysql/conf.d/mysqld_safe_syslog.conf  
  
ADD files/my.cnf /etc/mysql/my.cnf  
ADD files/scripts /usr/local/bin  
  
RUN \  
chmod 0640 /etc/mysql/my.cnf && \  
chmod +x /usr/local/bin/run.sh && \  
chown -R mysql:mysql /etc/mysql/  
  
EXPOSE 3306  
USER mysql  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/run.sh"]  

