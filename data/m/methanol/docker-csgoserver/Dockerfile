FROM ubuntu:14.04  
MAINTAINER Timo Schrappe <hello@timo.ruhr>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
curl \  
lib32gcc1 \  
ca-certificates  
  
RUN useradd -ms /bin/bash csgo  
USER csgo  
WORKDIR /home/csgo  
RUN curl -sqL
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz | tar
zxvf -  
RUN mkdir ~/.steam && ln -s /home/csgo/linux32 /home/csgo/.steam/sdk32  
COPY ./start-csgoserver.sh /usr/local/bin/start-csgoserver.sh  
  
USER root  
RUN chmod +x /usr/local/bin/start-csgoserver.sh  
  
# game transmission, pings and RCON  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  
  
# SourceTV transmission  
EXPOSE 27020/udp  
  
# unkown  
EXPOSE 27005/udp  
  
  
USER csgo  
ENTRYPOINT ["/bin/bash", "-c", "/usr/local/bin/start-csgoserver.sh", "--"]  

