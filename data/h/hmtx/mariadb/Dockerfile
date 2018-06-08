FROM mariadb:latest  
ENV MYSQL_RANDOM_ROOT_PASSWORD=yes  
ENV MYSQL_DATABASE=schild-test  
ENV MYSQL_USER=schild  
ENV MYSQL_PASSWORD=schild  
  
ADD schild-test.sql /docker-entrypoint-initdb.d/schild-test.sql  

