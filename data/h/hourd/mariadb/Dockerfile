FROM alpine:edge  
MAINTAINER Daniel Atkinson <hourd.tasa@gmail.com>  
  
RUN apk --update add \  
mariadb \  
mariadb-client  
  
ADD mariadb_init.sh /mariadb_init.sh  
ADD run.sh /run.sh  
RUN chmod 775 *.sh  
  
ADD my.cnf /etc/mysql/my.cnf  
  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
ENV TERM dumb  
  
CMD ["sh", "run.sh"]  
  
EXPOSE 3306  

