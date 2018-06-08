#  
# Dockerfile for shoutcast  
#  
# VERSION 0.1  
FROM debian:jessie-slim  
  
MAINTAINER Riftbit ErgoZ <ergozru@riftbit.com>  
  
WORKDIR /opt/shoutcast  
  
# Prepare APK CDNs  
RUN apt-get update && \  
apt-get install -y curl && \  
curl
http://download.nullsoft.com/shoutcast/tools/sc_serv2_linux_x64-latest.tar.gz
| tar xz && \  
mkdir -p control logs configs && \  
apt-get purge --auto-remove -y curl && \  
rm -rf /var/lib/apt/lists/*  
  
COPY sc_serv.conf ./configs  
  
#do not forget about /opt/shoutcast/sc_serv.conf  
VOLUME ["/opt/shoutcast/logs", "/opt/shoutcast/control",
"/opt/shoutcast/configs"]  
  
EXPOSE 8000:8000/tcp 8001:8001/tcp  
  
CMD ["./sc_serv", "./configs/sc_serv.conf"]  

