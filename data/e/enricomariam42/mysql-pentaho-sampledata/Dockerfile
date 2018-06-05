# Docker image based on mysql with sampledata db for pentaho biserver examples  
#  
# VERSION 1.0  
FROM mysql:5.6  
MAINTAINER Enrico Maria Carmona, e.carmona@hsgerardo.org  
  
# db-specific script files for pentaho biserver sampledata  
ADD sampledata/4_create_sample_tables_myql.sql /docker-entrypoint-
initdb.d/4_create_sample_tables_myql.sql  
ADD sampledata/5_load_sampledata_mysql.sql /docker-entrypoint-
initdb.d/5_load_sampledata_mysql.sql  
  

