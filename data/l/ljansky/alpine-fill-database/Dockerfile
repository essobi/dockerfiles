FROM ljansky/alpine-mysql-liquibase:latest  
  
COPY liquibase.properties /tmp/liquibase.properties  
COPY changelog.xml /tmp/changelog.xml  
COPY fill_database.sh /tmp/fill_database.sh  
RUN chmod 777 /tmp/fill_database.sh

