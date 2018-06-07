FROM java:8  
WORKDIR /opt/orient/  
  
RUN wget -nv -O - http://orientdb.com/download.php?file=orientdb-
community-2.1.1.tar.gz | tar -zx --strip-components=1 --directory /opt/orient  
  
ENV ORIENTDB_HOME="/opt/orient" ORIENTDB_ROOT_PASSWORD="root"  
EXPOSE 2424 2480 5701  
RUN ./bin/console.sh "create database plocal:$ORIENTDB_HOME/databases/default
admin admin plocal"  
  
RUN sed -i "s/value=\"SQL\"/value=\"SQL,Javascript\"/g" ./config/orientdb-
server-config.xml  
  
ENTRYPOINT ["./bin/server.sh"]  

