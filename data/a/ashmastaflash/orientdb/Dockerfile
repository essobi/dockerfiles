# OrientDB on JDK7,Ubuntu14.10  
# Heavily based on joaodubas/orientdb  
FROM ashmastaflash/openjdk  
MAINTAINER Ash Wilson  
  
ENV ORIENTDB_VERSION 2.0.8  
ENV ORIENTDB_URL
http://orientdb.com/download.php?email=unknown@unknown.com&file=orientdb-
community-${ORIENTDB_VERSION}.tar.gz&os=linux  
ENV ORIENTDB_ROOT_PASSWORD 0r13ntDB  
ADD ${ORIENTDB_URL} /usr/local/src/orientdb-community.tar.gz  
RUN cd /usr/local/src \  
&& tar -xzf orientdb-community.tar.gz \  
&& ln -s ${PWD}/orientdb-community-${ORIENTDB_VERSION} ${PWD}/orientdb \  
&& ln -s ${PWD}/orientdb/bin/* /usr/local/bin/ \  
&& rm ${PWD}/orientdb-community.tar.gz \  
&& mkdir /usr/local/log  
  
# configure system  
EXPOSE 2424  
EXPOSE 2480  
CMD ["/usr/local/bin/server.sh"]  

