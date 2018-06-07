FROM fedora:22  
MAINTAINER Ermanno Scaglione <erm67@yahoo.it>  
RUN dnf -y update && dnf -y install mariadb-server hostname && dnf clean all  
ADD mariadb-server.cnf /etc/my.cnf.d/mariadb-server.cnf  
EXPOSE 3306  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
USER mysql  
VOLUME ["/var/run/mariadb/"]  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["mysqld"]  

