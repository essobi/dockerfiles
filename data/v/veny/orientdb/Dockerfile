FROM veny/jdk  
MAINTAINER Vaclav Sykora <vaclav.sykora@gmail.com>  
  
ENV ORIENTDB_VERSION 2.2.11  
ENV ORIENTDB_DOWNLOAD_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=orientdb-
community-${ORIENTDB_VERSION}.tar.gz&os=linux  
ENV ORIENTDB_HOME /opt/orientdb  
ENV PATH $PATH:$ORIENTDB_HOME/bin  
  
ADD ${ORIENTDB_DOWNLOAD_URL} /tmp/orientdb.tar.gz  
  
RUN mkdir -p ${ORIENTDB_HOME} \  
&& tar xvzf /tmp/orientdb.tar.gz --strip-components=1 --directory
${ORIENTDB_HOME} \  
&& rm -f /tmp/orientdb.tar.gz \  
&& rm -rf ${ORIENTDB_HOME}/databases/*  
  
VOLUME ["${ORIENTDB_HOME}/backup", "${ORIENTDB_HOME}/config",
"${ORIENTDB_HOME}/databases", "${ORIENTDB_HOME}/log"]  
  
# binary, HTTP  
EXPOSE 2424 2480  
WORKDIR ${ORIENTDB_HOME}  
  
CMD ["./bin/server.sh"]  

