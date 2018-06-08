FROM busybox  
VOLUME /mumble  
  
COPY mumble-server.ini /mumble/mumble-server.ini  
COPY mumble-server.sqlite /mumble/mumble-server.sqlite  
RUN chown -R 107:109 /mumble  

