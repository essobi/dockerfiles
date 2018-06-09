# Teamspeak3 Server  
FROM debian:latest  
  
MAINTAINER ziermmar  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get -y install wget bzip2 sudo libmariadb2 libxml2-utils \  
&& mkdir -p /data \  
&& useradd -M -s /bin/false \--uid 1000 teamspeak3 \  
&& chmod -R 774 /data \  
&& chown -R teamspeak3:teamspeak3 /data  
  
COPY teamspeak3-start.sh /teamspeak3-start  
COPY initialize.sh /initialize  
  
VOLUME /data  
WORKDIR /data  
  
ENV TEAMSPEAK_UID 1000  
ENV TEAMSPEAK_GID 1000  
ENV TEAMSPEAK_INIFILE ts3server.ini  
  
CMD ["/initialize"]  
  
EXPOSE 9987/udp 10011 30033  

