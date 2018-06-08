FROM osrm/osrm-backend  
RUN apk add --no-cache curl  
  
RUN mkdir /data && \  
curl http://download.geofabrik.de/europe/netherlands-latest.osm.pbf --output
/data/netherlands-latest.osm.pbf && \  
osrm-extract -p /opt/car.lua /data/netherlands-latest.osm.pbf && \  
osrm-partition /data/netherlands-latest.osrm && \  
osrm-customize /data/netherlands-latest.osrm && \  
rm -rf /data/netherlands-latest.osm.pbf  
  
ENTRYPOINT osrm-routed --algorithm mld --max-table-size 10000
/data/netherlands-latest.osrm  

