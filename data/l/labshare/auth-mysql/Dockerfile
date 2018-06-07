FROM mysql:5.7.15  
  
ENV MYSQL_DATABASE=labshare \  
MYSQL_ALLOW_EMPTY_PASSWORD=true  
# Add MySQL auth schema  
ADD ./schema.sql /docker-entrypoint-initdb.d/  
  
EXPOSE 3306  

