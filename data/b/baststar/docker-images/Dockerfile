FROM osrm/osrm-backend  
LABEL org.freenas.interactive="false" \  
org.freenas.version="0.0.1" \  
org.freenas.upgradeable="false" \  
org.freenas.command="osrm/osrm-backend osrm-extract -p /opt/car.lua
/data/berlin-latest.osm.pbf" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="false" \  
org.freenas.port-mappings="5000:5000/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Data storage\" \  
} \  
]" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=5000 \  
org.freenas.web-ui-path="localhost:5000" \  
  
  

