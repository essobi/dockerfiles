FROM mdillon/postgis:9.2  
MAINTAINER Mike Cowgill <moofish32@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /docker-entrypoint-initdb.d  
  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  

