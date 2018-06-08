FROM elixir:latest  
  
# Nodejs  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
# From https://docs.docker.com/engine/examples/postgresql_service/  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5  
  
USER postgres  
RUN /etc/init.d/postgresql start && psql --command "ALTER USER postgres WITH
ENCRYPTED PASSWORD 'postgres';"  

