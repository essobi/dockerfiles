FROM java:openjdk-8  
ENV ORIENTDB_VERSION 2.1.2  
ENV ORIENTDB_FULL_VERSION orientdb-community-$ORIENTDB_VERSION  
ENV ORIENTDB_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=${ORIENTDB_FULL_VERSION}.tar.gz&os=linux  
  
RUN mkdir /orientdb; \  
wget -O $ORIENTDB_FULL_VERSION.tar.gz "$ORIENTDB_URL"; \  
tar -xvzf $ORIENTDB_FULL_VERSION.tar.gz -C /orientdb --strip-components=1; \  
ln -s /orientdb/bin/* /usr/local/bin/; \  
mkdir /usr/local/log; \  
rm $ORIENTDB_FULL_VERSION.tar.gz  
  
# VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]  
EXPOSE 2424  
EXPOSE 2480  
CMD ["/orientdb/bin/server.sh"]

