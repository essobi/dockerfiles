FROM postgres:latest  
MAINTAINER Scott Chamberlain <myrmecocystus@gmail.com>  
  
RUN apt-get update && apt-get install -y unzip curl \  
curl --silent "https://www.itis.gov/downloads/itisPostgreSql.zip" \  
&& unzip -Lj itisPostgreSql.zip  
  
USER postgres  
RUN /etc/init.d/postgresql start && psql -U postgres -f ITIS.sql  
  
EXPOSE 5432  

