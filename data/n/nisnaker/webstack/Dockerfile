FROM alpine:latest  
  
MAINTAINER https://github.com/nisnaker/webstack  
  
RUN apk -U add mariadb mariadb-client \  
&& rm /etc/mysql/my.cnf  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY entrypoint.sh /usr/local/bin/  
  
VOLUME ["/var/lib/mysql", "/var/lib/backup"]  
  
ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

