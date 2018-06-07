FROM alpine:latest  
  
# create regular user  
RUN addgroup -S -g 5000 syncthing \  
&& adduser -S -h /data -H -s /sbin/nologin -G syncthing -D -u 5000 syncthing \  
&& mkdir -p /data \  
&& chown -R syncthing:syncthing /data  
  
# install the services  
RUN apk --update --no-cache add \  
syncthing  
  
EXPOSE 8384 22000 21027/udp  
  
USER syncthing  
  
ENTRYPOINT ["syncthing"]  
CMD ["-logfile", "/data/syncthing.log", "-home", "/data", "-gui-address",
"http://0.0.0.0:8384"]  

