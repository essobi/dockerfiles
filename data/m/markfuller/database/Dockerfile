FROM mariadb:10.2  
COPY config/utf8mb4.cnf /etc/mysql/conf.d/utf8mb4.cnf  
  
ENV MYSQL_DATABASE drupal  
ENV MYSQL_USER drupal  
ENV MYSQL_PASSWORD my-secret-password  
ENV MYSQL_ROOT_PASSWORD my-secret-password  
  
EXPOSE 3306  
CMD ["mysqld"]

