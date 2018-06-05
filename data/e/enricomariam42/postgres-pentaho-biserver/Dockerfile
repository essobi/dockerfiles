# Docker image based on postgresql customized for pentaho biserver  
#  
# VERSION 1.0  
FROM postgres:9.3  
MAINTAINER Enrico Maria Carmona, e.carmona@hsgerardo.org  
  
# db-specific script files for pentaho biserver  
ADD pentaho-biserver-5/create_jcr_postgresql.sql /docker-entrypoint-
initdb.d/01_create_jcr_postgresql.sql  
ADD pentaho-biserver-5/create_quartz_postgresql.sql /docker-entrypoint-
initdb.d/02_create_quartz_postgresql.sql  
ADD pentaho-biserver-5/create_repository_postgresql.sql /docker-entrypoint-
initdb.d/03_create_repository_postgresql.sql  
ADD pentaho-biserver-5/dummy_quartz_table.sql /docker-entrypoint-
initdb.d/04_dummy_quartz_table.sql  

