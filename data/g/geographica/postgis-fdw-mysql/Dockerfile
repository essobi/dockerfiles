FROM geographica/postgis:latest  
  
MAINTAINER Alberto Asuero "alberto@geographica.gs"  
  
RUN apt-get -y update && \  
apt-get -y install git libmysqlclient-dev && \  
git clone https://github.com/EnterpriseDB/mysql_fdw.git && \  
cd mysql_fdw && make USE_PGXS=1 && make USE_PGXS=1 install && \  
cd .. && rm -R mysql_fdw  

