FROM lsiobase/alpine.arm64:latest  
  
COPY \--from=resin/aarch64-alpine:latest ["/usr/bin/qemu*", "/usr/bin/resin-
xbuild*", "/usr/bin/cross-build*", "/usr/bin/"]  
  
RUN [ "cross-build-start" ]  
RUN apk add --no-cache nfs-utils  
  
RUN [ "cross-build-end" ]  
  
COPY s6/config.init /etc/cont-init.d/00-config  
COPY s6/rpcbind.run /etc/services.d/rpcbind/run  
COPY s6/mountd.run /etc/services.d/mountd/run  
  
EXPOSE 111/udp 2049/tcp 2049/udp  
  
CMD ["/init"]  

