FROM efrecon/mini-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Install git so we can install dependencies  
# Install tsdb into /opt and til in the lib subdirectory  
RUN apk add --update-cache git && \  
git clone https://github.com/efrecon/tsdb /opt/tsdb && \  
rm -rf /opt/tsdb/.git && \  
git clone https://github.com/efrecon/til /opt/tsdb/lib/til && \  
rm -rf /opt/tsdb/lib/til/.git && \  
apk del git && \  
rm -rf /var/cache/apk/*  
  
# Export Graphite and Influx ports  
EXPOSE 2003  
EXPOSE 8086  
# Export where databases will be placed by default  
VOLUME /data  
  
# Execute tsdb on start, listening for both client APIs connections on  
# default database called data (meaning that it will create a  
# subdirectory itself called data in the rootdirectory /data,  
# i.e. /data/data).  
ENTRYPOINT ["tclsh8.6", "/opt/tsdb/tsdb.tcl", "-root", "/data", "-dbs",
"data", "-ports", "graphite:data:2003 influx:data:8086"]  
CMD ["-v", "3"]  

