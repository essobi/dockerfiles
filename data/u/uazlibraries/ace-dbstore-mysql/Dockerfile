FROM mysql:5.7  
  
COPY docker/ /opt/ace-dbstore/  
RUN \  
mv -v /opt/ace-dbstore/create-db.sh /docker-entrypoint-initdb.d/ && \  
mv -v /opt/ace-dbstore/large-index.cnf /etc/mysql/mysql.conf.d/  
  

