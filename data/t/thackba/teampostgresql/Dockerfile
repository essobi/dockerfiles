FROM thackba/java:latest  
MAINTAINER mail@thackbarth.net  
  
ARG CONTAINER_UID=1300  
ARG CONTAINER_GID=1300  
COPY entrypoint.sh /  
  
RUN export CONTAINER_USER=team && \  
export CONTAINER_GROUP=team && \  
addgroup -gid $CONTAINER_GID $CONTAINER_GROUP && \  
adduser --system --home /home/$CONTAINER_USER \--shell /bin/bash --uid
$CONTAINER_UID \--ingroup $CONTAINER_GROUP $CONTAINER_USER && \  
apt-get update && \  
apt-get install -y apt-utils curl unzip && \  
curl http://cdn.webworks.dk/download/teampostgresql_multiplatform.zip -o
/teampostgresql_multiplatform.zip && \  
unzip /teampostgresql_multiplatform.zip && \  
rm /teampostgresql_multiplatform.zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/* /tmp/* /var/tmp/* /var/cache/apt/* && \  
chown -R team:team /teampostgresql && \  
chmod 755 /teampostgresql/teampostgresql-run.sh && \  
chmod 755 /entrypoint.sh  
  
USER team  
  
EXPOSE 8082  
CMD ["/entrypoint.sh", "teampostgresql"]  
  

