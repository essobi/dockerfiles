FROM mysql:5.6  
COPY plaza.cnf /etc/mysql/conf.d/plaza.cnf  
COPY timezone /etc/timezone  
#COPY update_timezone.sh /docker-entrypoint-initdb.d/update_timezone.sh  
VOLUME /data  
  
ENV TZ 'Australia/Melbourne'  
ENV MYSQL_ROOT_PASSWORD=password  

