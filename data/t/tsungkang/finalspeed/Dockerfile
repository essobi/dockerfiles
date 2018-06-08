#  
# Dockerfile for finalspeed  
#  
FROM java:latest  
  
MAINTAINER fs <d1sm@ip4a.com>  
  
ENV FS_DIR /fs  
ENV FS_DEP unzip libpcap-dev iptables  
  
USER root  
  
RUN \  
if [ ! -d "$FS_DIR" ]; then mkdir $FS_DIR; fi && \  
apt-get update && \  
apt-get install -y $FS_DEP  
  
ENV SERVER_PORT 150  
EXPOSE $SERVER_PORT  
EXPOSE $SERVER_PORT/udp  
  
WORKDIR $FS_DIR  
ADD fs.jar /  
ADD entrypoint /  
RUN chmod +x /entrypoint  
ENTRYPOINT ["/entrypoint"]  
CMD ["-h"]

