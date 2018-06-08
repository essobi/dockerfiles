# Orientdb  
#  
FROM java:latest  
MAINTAINER Loïc Tosser "wowi@wowi.io"  
# install OrientDB  
ENV ORIENTDB_VERSION orientdb-community-2.0.11  
ENV ORIENTDB_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=${ORIENTDB_VERSION}.tar.gz&os=linux  
ENV ORIENTDB_ROOT_PASSWORD 0r13ntDB  
ENV ORIENTDB_NODE_NAME Uranus  
ADD ${ORIENTDB_URL} /usr/local/src/orientdb-community.tar.gz  
WORKDIR /usr/local/src  
RUN tar -xzf orientdb-community.tar.gz  
RUN mv ${ORIENTDB_VERSION} orientdb  
RUN rm orientdb-community.tar.gz  
RUN mkdir /usr/local/log  
VOLUME /usr/local/src/orientdb/config  
VOLUME /usr/local/src/orientdb/databases  
VOLUME /usr/local/src/orientdb/log  
# configure system  
EXPOSE 2424  
EXPOSE 2434  
EXPOSE 2480  
CMD ["/usr/local/src/orientdb/bin/dserver.sh"]  

