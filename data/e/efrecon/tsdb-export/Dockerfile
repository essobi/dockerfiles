FROM efrecon/mini-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Install git so we can install dependencies  
# Install tsdb into /opt and til in the lib subdirectory  
RUN apk add --update-cache git && \  
git clone https://github.com/efrecon/tsdb /opt/tsdb && \  
rm -rf /opt/tsdb/.git && \  
apk del git && \  
rm -rf /var/cache/apk/*  
  
# Export where databases will be placed by default  
VOLUME /data  
  
# Execute export on start, Use same directory conventions as the  
# main tsdb process  
ENTRYPOINT ["tclsh8.6", "/opt/tsdb/export.tcl", "-root", "/data", "-dbs",
"data"]  
CMD ["-v", "5"]  

