FROM efrecon/mini-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Install git so we can install tcl-stomp  
# Install tcl-stomp into /tmp and move it to a proper location  
RUN apk add \--update-cache git && \  
git clone https://github.com/efrecon/tcl-stomp /opt/stomp && \  
rm -rf /opt/stomp/.git && \  
apk del git && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["tclsh8.6", "/opt/stomp/printer.tcl"]  

