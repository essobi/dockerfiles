# Creates a postgres empty database with ambari schema for Amabri Server
development  
FROM postgres  
MAINTAINER SequenceIQ  
  
# set up ambari database; ambari database user/password, roles and privileges  
ENV PGDATA /var/lib/ambari/psql/data  
  
# ambari database  
ENV POSTGRES_DB ambari  
  
# ambari database user  
ENV POSTGRES_USER ambari  
  
# ambari database user password  
ENV POSTGRES_PASSWORD bigdata  
  
ENV VER trunk  
  
# download amabri schema creation sql  
RUN apt-get update && apt-get install -y curl \  
&& curl -L -o /docker-entrypoint-initdb.d/amabri_schema_create.sql
https://raw.githubusercontent.com/apache/ambari/$VER/ambari-
server/src/main/resources/Ambari-DDL-Postgres-CREATE.sql \  
&& echo "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;" >>
/docker-entrypoint-initdb.d/amabri_schema_create.sql \  
&& echo "ALTER DATABASE $POSTGRES_DB OWNER TO $POSTGRES_USER;" >> /docker-
entrypoint-initdb.d/amabri_schema_create.sql  

