  
FROM postgres:9.1.20  
ADD initdb.sh /docker-entrypoint-initdb.d/  
RUN chmod +x /docker-entrypoint-initdb.d/initdb.sh  
RUN sed -i "/postgres \/run\/postgresql/a chown -R postgres
/var/lib/postgresql" /docker-entrypoint.sh  

