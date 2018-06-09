# Run intel-sdi snapd  
# what's up with that?  
#FROM gliderlabs/alpine:3.3  
# OH god. snapd is dynamically linked.  
#  
FROM ubuntu:16.04  
EXPOSE 8181  
RUN mkdir -p /opt/snap/src  
  
ADD https://github.com/sandlbn/intelsdi-snap/raw/master/snap.tgz
/opt/snap/src/  
  
# Docker unpacked the snap files when they're local  
RUN tar -zxvf /opt/snap/src/snap.tgz -C /  
  
ENTRYPOINT ["/opt/snap/bin/snapd", "--api-port", "8181", "--log-level", "2", "
--auto-discover", "/opt/snap/plugin", "-t", "0" ]  

