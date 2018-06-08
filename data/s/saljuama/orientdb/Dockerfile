############################################  
# Dockerfile to run an OrientDB database #  
############################################  
  
FROM java:8  
  
MAINTAINER Salvador Juan Martínez "saljuama@gmail.com"  
  
ENV ORIENTDB_VERSION 2.1.12  
ENV ORIENTDB_DOWNLOAD_URL
"http://orientdb.com/download.php?email=unknown@unknown.com&file=orientdb-
community-${ORIENTDB_VERSION}.tar.gz&os=linux"  
  
RUN mkdir /orientdb \  
&& curl -o orientdb-community.tar.gz ${ORIENTDB_DOWNLOAD_URL} \  
&& tar -xzf orientdb-community.tar.gz -C /orientdb --strip-components=1 \  
&& rm orientdb-community.tar.gz \  
&& rm -rf /orientdb/databases/*  
  
VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]  
  
EXPOSE 2424  
EXPOSE 2480  
  
ENV ORIENTDB_ROOT_PASSWORD s3cr3t  
  
CMD ["/orientdb/bin/server.sh"]  

