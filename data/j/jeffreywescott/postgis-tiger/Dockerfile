FROM mdillon/postgis:9.6  
MAINTAINER Jeffrey Wescott <jeffrey.wescott@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y unzip  
  
RUN mkdir -p /gisdata/temp  
RUN chmod -R 777 /gisdata  
RUN mkdir -p /docker-entrypoint-initdb.d  
RUN mkdir -p /scripts  
ADD scripts/ /scripts/  
  
RUN mv /docker-entrypoint-initdb.d/postgis.sh /docker-entrypoint-
initdb.d/000-postgis.sh  
ADD init/ /docker-entrypoint-initdb.d/  

