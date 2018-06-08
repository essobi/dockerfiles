FROM postgres:9.4.1  
MAINTAINER Powell Kinney <powell@vin.li>  
  
RUN apt-get update \  
&& apt-get -y install postgresql-contrib-9.4 postgresql-9.4-postgis-2.1
postgis \  
&& rm -rf /var/lib/apt/lists/*  

