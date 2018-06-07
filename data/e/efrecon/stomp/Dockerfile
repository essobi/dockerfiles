FROM efrecon/mini-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Install git so we can install tcl-stomp  
# Install tcl-stomp into /tmp and move it to a proper location  
RUN apk add --update-cache git && \  
git clone https://github.com/efrecon/tcl-stomp /opt/stomp && \  
rm -rf /opt/stomp/.git && \  
apk del git && \  
rm -rf /var/cache/apk/*  
  
# Expose STOMP port and data volume  
EXPOSE 61613  
VOLUME /data  
  
# New entrypoint! the server itself, nothing else so we can give it  
# options through CMD (or from compose or similar tool)  
ENTRYPOINT ["tclsh8.6", "/opt/stomp/stompserver.tcl"]  

