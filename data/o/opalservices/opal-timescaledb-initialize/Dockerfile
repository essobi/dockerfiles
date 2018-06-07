FROM
ubuntu:16.04@sha256:7a3b062531155aa4aee0f0e01a3f4440c86dcf972b1b73ec5d988ae438bb2651  
MAINTAINER Shubham Jain <s.jain@imperial.ac.uk>  
  
WORKDIR /root  
  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \  
&& apt-get install -y git \  
&& apt-get install -y postgresql-client  
  
RUN git clone https://github.com/OPAL-Project/OPAL-Database.git  
  
CMD sleep 2 ; psql -h timescaledb -U postgres -tc "SELECT 1 FROM pg_database
WHERE datname = 'opal'" | grep -q 1 || psql -h timescaledb -U postgres -c
"CREATE DATABASE opal" ; psql -h timescaledb opal postgres -f OPAL-
Database/timescaledb/timescale.sql  

