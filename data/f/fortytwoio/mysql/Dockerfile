## Version 1.0.3  
FROM fortytwoio/base:latest  
MAINTAINER Thomas Fritz <thomas.fritz@forty-two.io>  
  
ADD http://repo.mysql.com/mysql-apt-config_0.2.1-1debian7_all.deb /tmp/mysql-
apt-config.deb  
RUN DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/mysql-apt-config.deb  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqy > /dev/null 2>&1 && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qqy --no-install-recommends
perl mysql-server > /dev/null 2>&1  
  
ADD ./etc/mysql/my.cnf /etc/mysql/my.cnf.tpl  
  
EXPOSE 3306  
VOLUME ["/var/lib/mysql"]  

