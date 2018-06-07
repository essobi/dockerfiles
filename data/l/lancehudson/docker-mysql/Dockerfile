FROM mysql:5.7.8-rc  
ENV MYSQL_IMPORT /usr/local/mysql/scripts/import.sql  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ONBUILD COPY import.sql /usr/local/mysql/scripts/import.sql  

