FROM mysql/mysql-server:5.5  
MAINTAINER Ian.Lintner@Workiva.com  
  
#This is for dev instances only set this if using in production!  
ENV MYSQL_USER admin  
ENV MYSQL_PASSWORD admin  
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes  
  
COPY config/mysql/my.cnf /etc/my.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 775 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

