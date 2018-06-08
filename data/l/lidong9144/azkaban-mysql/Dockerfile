FROM mysql:5.7.17  
  
COPY mysql.cnf /etc/mysql/conf.d/  
  
#COPY init.sh /mysql/init.sh  
COPY init.sql /docker-entrypoint-initdb.d/init.sql  

