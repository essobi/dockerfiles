FROM mysql  
MAINTAINER Daniel Guerra  
  
COPY create-user.sql /docker-entrypoint-initdb.d/create-user.sql  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld","--character-set-server=utf8mb4","--collation-
server=utf8mb4_unicode_ci","--explicit_defaults_for_timestamp=UTC"]  

