ARG INFLUX_TAG=alpine  
  
FROM influxdb:${INFLUX_TAG}  
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>  
  
# Add base tcl distribution and copy backup script  
RUN apk --no-cache add tcl  
COPY backup.tcl /usr/local/bin/  
  
# Export /backup volume which is the default root for backups.  
VOLUME ["/backup"]  
  
# Default entry point is backup, this easily skips any cmd/entrypoint that
would  
# inherit from the original influx image so no daemon is started or  
# initialisation performed.  
ENTRYPOINT ["tclsh8.6", "/usr/local/bin/backup.tcl"]

