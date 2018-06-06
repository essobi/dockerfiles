FROM mdillon/postgis:9.4  
MAINTAINER Cityway  
  
LABEL Description="Chouette DB" \  
Usage="docker run --name chouette-postgres -p 5433:5432 -e
POSTGRES_USER=chouette -e POSTGRES_PASSWORD=chouette -d chouette-postgres" \  
BuildUsage="docker build -t chouette-postgres ." \  
License="CECILL/B" \  
Version="3.0"  
  
COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
  

