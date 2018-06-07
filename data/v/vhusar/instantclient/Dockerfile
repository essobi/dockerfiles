FROM alpine:3.6  
  
ENV LANG=C.UTF-8 \  
JAVA_HOME=/opt/java \  
LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH \  
PATH=/opt/oracle/instantclient_12_2:$PATH \  
TNS_ADMIN=/opt/oracle/instantclient_12_2 \  
ORACLE_BASE=/opt/oracle/instantclient_12_2 \  
ORACLE_HOME=/opt/oracle/instantclient_12_2  
  
ENV ORACLE_BASE /usr/lib/instantclient_12_2  
ENV ORACLE_HOME /usr/lib/instantclient_12_2  
  
COPY ./fs /  
  
RUN apk add \--no-cache bash libaio && \  
apk add \--no-cache --virtual .build-deps ca-certificates wget && \  
wget -O - https://raw.githubusercontent.com/viliam-husar/docker-alpine-
shared/master/install-glibc-v1.sh | sh && \  
wget -O - https://raw.githubusercontent.com/viliam-husar/docker-alpine-
shared/master/install-oracle-java-se-jre-v1.sh | sh && \  
mkdir -p /opt/oracle && \  
unzip /tmp/instantclient_packages/instantclient-basic-linux.x64-12.2.0.1.0.zip
-d /opt/oracle && \  
unzip /tmp/instantclient_packages/instantclient-sqlplus-
linux.x64-12.2.0.1.0.zip -d /opt/oracle && \  
cd /opt/oracle/instantclient_12_2 && \  
ln -s libclntsh.so.12.1 libclntsh.so && \  
ln -s libocci.so.12.1 libocci.so && \  
cd / && \  
apk del .build-deps && \  
rm -rf /tmp/instantclient_packages  
  
CMD ["sqlplus"]

