FROM java:8-jre  
MAINTAINER Kha Nguyen <nlhkha@gmail.com>  
WORKDIR /usr/src  
ENV ORIENTDB_VERSION orientdb-community-2.1.3  
ENV ORIENTDB_ROOT_PASSWORD 0r13ntDB  
RUN wget
"http://orientdb.com/download.php?file=${ORIENTDB_VERSION}.tar.gz&os=linux" -O
orientdb-install.tar.gz  
RUN tar -xzf orientdb-install.tar.gz  
RUN rm orientdb-install.tar.gz  
RUN mv ${ORIENTDB_VERSION} /usr/local/orientdb  
WORKDIR /usr/local/orientdb  
VOLUME /usr/local/orientdb/databases  
EXPOSE 2424  
EXPOSE 2480  
CMD ["bin/server.sh"]  

