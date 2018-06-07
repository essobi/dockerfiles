FROM mysql:5.6  
ENV MYSQL_ROOT_PASSWORD=mysql  
  
RUN apt-get update && apt-get install -y gettext  
  
ADD 0-empty.sql /docker-entrypoint-initdb.d  
ADD jira7.sql /prepare/init.sql  
COPY docker-entrypoint-mod.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh /prepare/init.sql  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["mysqld"]  

