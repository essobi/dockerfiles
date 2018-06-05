FROM jgoerzen/ampache  
MAINTAINER John Goerzen <jgoerzen@complete.org>  
RUN mv /usr/sbin/policy-rc.d.disabled /usr/sbin/policy-rc.d  
RUN apt-get update && \  
apt-get -y --no-install-recommends install mysql-server && \  
apt-get -y -u dist-upgrade && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN /usr/local/bin/docker-wipelogs  
RUN mv /usr/sbin/policy-rc.d /usr/sbin/policy-rc.d.disabled  
RUN /etc/init.d/mysql start && sleep 10 && \  
while [ ! -e /var/run/mysqld/mysqld.sock ]; do sleep 1; done; sleep 1 && \  
mysql -e 'CREATE DATABASE ampache' && \  
mysql -e "GRANT ALL on ampache.* TO 'ampache'@'localhost' IDENTIFIED BY
'ampache'" && \  
mysql -e "FLUSH PRIVILEGES" && \  
/etc/init.d/mysql stop  
  
EXPOSE 80 443 81  
VOLUME ["/var/lib/mysql", "/var/www/ampache/config"]  
CMD ["/usr/local/bin/boot-debian-base"]  
  

