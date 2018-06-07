FROM mariadb:5.5  
## The maintainer name and email  
MAINTAINER Igor Lakic <trzalica87@gmail.com>  
  
# Docksal settings  
COPY default.cnf /etc/mysql/conf.d/10-default.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

