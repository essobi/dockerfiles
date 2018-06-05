FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y curl xz-utils postgresql  
  
WORKDIR /opt  
RUN curl -L
https://github.com/begriffs/postgrest/releases/download/v0.3.0.1/postgrest-0.3.0.1-ubuntu.tar.xz
| tar xJ  
  
ADD ./pgr.sh /opt/pgr.sh  
  
CMD /opt/postgrest
postgres://postgres:$POSTGRES_ENV_POSTGRES_PASSWORD@$POSTGRES_PORT_5432_TCP_ADDR:$POSTGRES_PORT_5432_TCP_PORT/$POSTGRES_DB_NAME
\--schema $SCHEMA \--jwt-secret $JWT_SECRET \--port 8000 -a postgres --pool
$POOL_SIZE  

