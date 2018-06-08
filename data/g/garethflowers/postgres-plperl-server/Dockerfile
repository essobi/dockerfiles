FROM postgres:9.6.8  
  
LABEL maintainer=garethflowers \  
name=postgres-plperl-server \  
version=9.6.8  
  
ENV POSTGRES_INITDB_ARGS \--encoding='UNICODE' \--lc-collate='C' \--lc-
ctype='C'  
RUN apt-get update && \  
apt-get install -y postgresql-plperl-$PG_MAJOR && \  
rm -rf /var/lib/apt/lists/*  

