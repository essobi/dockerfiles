FROM hasufell/gentoo-mysql:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
## MYSQL  
# contains mysql script to initialize the pydio database  
COPY create_pydio_db.sql /mysql-scripts/create_pydio_db.sql  
  
# honour our PYDIO_DB_PW env variable  
RUN sed -i -e '/^ImportSql\\(\\)/ { n; s/.*/\\{\nsed -i -e
\"s\/@432#PASSWORD#432@\/\$\\{PYDIO_DB_PW\\}\/\" \/mysql-
scripts\/create_pydio_db\\.sql/ ; }' /run.sh  

