FROM znc:latest  
  
RUN apk add --no-cache tor proxychains-ng  
  
COPY 98-launch.sh my_entrypoint.sh ./  
  
VOLUME ["/tor-data"]  
  

