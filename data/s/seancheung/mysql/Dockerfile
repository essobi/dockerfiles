FROM alpine:3.5  
LABEL maintainer="Sean Cheung <theoxuanx@gmail.com>"  
  
RUN apk add --update --no-cache mysql mysql-client bash  
  
COPY entrypoint.sh /entrypoint.sh  
COPY my.cnf /etc/mysql/my.cnf  
  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/mysqld"]  

