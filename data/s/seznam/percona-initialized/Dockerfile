FROM percona:5.6  
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes  
  
RUN mkdir /var/lib/mysql2 && \  
sed -i "/exec /d" /docker-entrypoint.sh && \  
sed -i "s~/var/lib/mysql~/var/lib/mysql2~g" /etc/mysql/my.cnf  
  
RUN /docker-entrypoint.sh mysqld  
  
COPY *.sh /docker-mysql-tools/  
  
ENTRYPOINT mysqld  

