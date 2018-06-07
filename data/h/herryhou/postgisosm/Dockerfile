FROM mdillon/postgis:9.5  
RUN apt-get update && \  
apt-get install -y --no-install-recommends osm2pgsql && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./importOSM.sh /importOSM.sh  
RUN chmod +x /importOSM.sh  
COPY ./postgis-vt-util.sql /postgis-vt-util.sql

