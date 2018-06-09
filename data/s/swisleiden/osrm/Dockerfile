FROM osrm/osrm-backend:latest  
  
LABEL maintainer "bjorn@swis.nl"  
  
EXPOSE 5000  
RUN mkdir /data && cd /data && wget --progress=dot:giga
http://download.geofabrik.de/europe-latest.osm.pbf && osrm-extract -p
/opt/car.lua /data/europe-latest.osm.pbf && osrm-contract /data/europe-
latest.osrm && rm /data/europe-latest.osm.pbf  
  
ENTRYPOINT osrm-routed /data/europe-latest.osrm

