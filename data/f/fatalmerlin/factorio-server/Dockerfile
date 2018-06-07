FROM debian:latest  
  
MAINTAINER fatalmerlin <merlin@fataldream.com>  
  
ENV UID=1000 GID=1000 VERSION=0.14.20  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y \  
sudo \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
  
COPY ["init.sh", "/init.sh"]  
COPY ["start.sh", "/start.sh"]  
COPY ["start-server.sh", "/start-server.sh"]  
  
RUN chmod +x /init.sh /start.sh /start-server.sh && sleep 1 && /init.sh  
  
EXPOSE 34197/udp  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/start.sh"]  

