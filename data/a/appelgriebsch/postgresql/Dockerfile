#  
# PostgreSQL Dockerfile  
# VERSION 9.6  
# Pull Alpine Linux stable base image  
FROM appelgriebsch/alpine:3.5  
MAINTAINER Andreas Gerlach <info@appelgriebsch.com>  
LABEL AUTHOR="Andreas Gerlach <info@appelgriebsch.com>"  
LABEL NAME="postgresql"  
LABEL VERSION="9.6"  
  
# bind to localhost only (will expose a socket for connection)  
ENV PGSQL_BIND 127.0.0.1  
# netmask for localhost only binding (specifies the network segment the server
listen to)  
ENV PGSQL_NETMASK 127.0.0.1/8  
# default tcp port for postgresql server  
ENV PGSQL_PORT 5432  
# default database user credentials <name:pwd> (name is lowercase)  
ENV PGSQL_DBADMIN pgadmin:pgAdmin123!  
# default database for user (dbname is lowercase)  
ENV PGSQL_DBNAME sampledb  
# log level of postgresql server  
ENV PGSQL_LOGLVL notice  
  
# install postgresql server  
USER root  
COPY postgresql.sh /tmp/  
RUN \  
mkdir -p /data/pgsql && \  
chown -R postgres:postgres /data/pgsql && \  
chmod -R 755 /data/pgsql && \  
chmod 755 /tmp/postgresql.sh  
  
# Define mountable directories.  
VOLUME /data/pgsql  
  
# Define working directory.  
WORKDIR /data/pgsql  
  
# Expose ports.  
EXPOSE $PGSQL_PORT  
  
# run service  
USER postgres  
ENTRYPOINT ["/tmp/start_instance.sh", "/tmp/postgresql.sh"]  

