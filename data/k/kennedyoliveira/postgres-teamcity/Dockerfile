FROM postgres:9.5  
MAINTAINER Kennedy Oliveira <kennedy.oliveira@outlook.com>  
  
# Creates the directory to store custom initialization scripts  
RUN mkdir -p /docker-entrypoint-initdb.d/  
  
# Copys initialization script  
COPY ["teamcity_database.sql", "/docker-entrypoint-initdb.d/"]  
  
# Copys script to update postgres configuration  
COPY ["update_postgres_conf.sh", "/docker-entrypoint-initdb.d/"]

