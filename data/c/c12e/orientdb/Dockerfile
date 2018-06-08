############################################################  
# Dockerfile to run an OrientDB (Graph) Container  
############################################################  
  
FROM c12e/debian  
MAINTAINER CognitiveScale.com  
  
ENV SERVICE_NAME=orientdb  
ADD supervisor.conf /etc/supervisor/conf.d/${SERVICE_NAME}.conf  
  
ENV ORIENTDB_VERSION 2.0-M2  
  
# Update the default application repository sources list  
# and Install OrientDB dependencies and supervisor  
RUN apt-get update && \  
apt-get -y install git ant maven supervisor apt-utils  
  
# Install Binaries  
RUN mkdir -p /tmp/build /data /logs && \  
cd /tmp/build && \  
git clone https://github.com/orientechnologies/orientdb.git --single-branch
--depth 1 --branch $ORIENTDB_VERSION && \  
git clone https://github.com/orientechnologies/orientdb-lucene.git --single-
branch --depth 1 --branch $ORIENTDB_VERSION&& \  
cd orientdb && \  
ant clean install && \  
mv /tmp/build/releases/orientdb-community-${ORIENTDB_VERSION} /opt && \  
ln -s /opt/orientdb-community-${ORIENTDB_VERSION} /opt/orientdb && \  
chmod a+x /opt/orientdb/bin/*.sh && \  
cd /tmp/build/orientdb-lucene && \  
mvn assembly:assembly && \  
mv /tmp/build/orientdb-lucene/target/orientdb-
lucene-${ORIENTDB_VERSION}-dist.jar \  
/opt/orientdb-community-${ORIENTDB_VERSION}/plugins && \  
sed -i '/<users>/a <user resources="*" password="root" name="root"/>'
/opt/orientdb/config/orientdb-server-config.xml && \  
rm -rf /tmp/build ~/.m2  
  
ADD GratefulDeadConcerts.* /opt/orientdb/GratefulDeadConcerts/  
# <entry value="C:/temp/databases" name="server.database.path" />  
  
#volume  
#VOLUME ['/data', '/logs']  
  
EXPOSE 2424  
EXPOSE 2480  
  
# Set the user to run OrientDB daemon  
USER root  
  
# Default command when starting the container  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

