#  
# PostgreSQL data container  
#  
# Pull base image.  
FROM debian:wheezy  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r postgres && useradd -r -g postgres postgres  
  
RUN mkdir -p /var/lib/postgresql/data && chown -R postgres
/var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data

