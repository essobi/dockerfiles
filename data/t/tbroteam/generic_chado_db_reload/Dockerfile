FROM ubuntu:trusty  
  
RUN apt-get update && apt-get \--assume-yes install \  
postgresql-client \  
postgresql-client-common  
  
ADD chado_database_complete.sql.tar.gz /tmp/  
CMD export PGPASSWORD="$CHADO_ENV_DB_PW"; \  
cat /tmp/chado_database_complete.sql | psql \--host=$CHADO_PORT_5432_TCP_ADDR
\--port=$CHADO_PORT_5432_TCP_PORT \--username=$CHADO_ENV_DB_USER
$CHADO_ENV_DB_NAME  

