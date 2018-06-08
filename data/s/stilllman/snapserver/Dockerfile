# docker run --rm  
# --name snapserver  
# -p 1704:1704 -p 1705:1705  
# -v /tmp/snapcast:/tmp  
# stilllman/docker-snapserver  
  
  
FROM debian:jessie  
RUN apt-get update \  
&& apt-get install wget -y \  
&& rm -rf /var/lib/apt/lists/*  
ENV snapcast_version 0.7.0  
RUN wget
https://github.com/badaix/snapcast/releases/download/v${snapcast_version}/snapserver_${snapcast_version}_amd64.deb  
RUN dpkg -i snapserver_${snapcast_version}_amd64.deb \  
; apt-get update \  
&& apt-get -f install -y \  
&& rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["snapserver"]  

