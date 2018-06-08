# orientdb  
FROM java:8  
MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>  
  
# env variables that best be changed by run command  
ENV ORIENTDB_ROOT_PASSWORD=changeme  
ENV HEAP_MEM_LIMIT=512M  
ENV DISK_CACHE_BUFFER=1536  
ENV ODB_NETWORK_LOCKTIMEOUT=30000  
ENV ODB_NETWORK_SOCKETTIMEOUT=30000  
# install orientdb  
ENV ORIENTDB_VERSION='2.1.18'  
ENV ORIENTDB_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=orientdb-
community-${ORIENTDB_VERSION}.tar.gz&os=linux  
ENV ORIENTDB_HOME='/opt/orientdb'  
ADD ${ORIENTDB_URL} /tmp/orientdb.tar.gz  
  
RUN mkdir -p ${ORIENTDB_HOME} \  
&& tar -zxvf /tmp/orientdb.tar.gz --strip-components=1 \--directory
${ORIENTDB_HOME} \  
&& ln -s ${ORIENTDB_HOME}/bin/* /usr/local/bin/ \  
&& rm -rf /tmp/ \  
&& rm -rf ${ORIENTDB_HOME}/databases/ \  
&& mkdir /usr/local/log  
  
ADD service.sh ${ORIENTDB_HOME}/  
VOLUME ${ORIENTDB_HOME}/databases/  
  
# configure system  
EXPOSE 2424  
EXPOSE 2480  
WORKDIR ${ORIENTDB_HOME}  
  
ENTRYPOINT ["./service.sh"]  

