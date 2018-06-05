# Wildfly server with additional configurations  
FROM postgres:9.5.4  
MAINTAINER Lucas Russo  
  
ENV SCRIPTS_VERSION 2.2.8-1  
# Add initial databases  
COPY scripts/init-user-db.sh /docker-entrypoint-initdb.d  
  
# Create schemas  
COPY scripts/${SCRIPTS_VERSION}/*.sql /docker-entrypoint-initdb.d/  

