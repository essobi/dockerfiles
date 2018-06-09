FROM debian:jessie  
  
MAINTAINER Adam Veldhousen <adam@veldhousen.ninja>, @adamveld12  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get -y install lib32gcc1 libstdc++6 libstdc++6:i386 curl ca-certificates
tar  
  
RUN useradd -m -s /bin/bash steam  
  
COPY ./configuration /configuration  
  
WORKDIR /home/steam  
  
RUN mkdir -p ./steamcmd/steacmd.sh && \  
mkdir /data && \  
curl http://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz |
tar -xz -C ./steamcmd/ && \  
echo quit | ./steamcmd/steamcmd.sh && \  
mkdir -p ./.steam/sdk32 && \  
ln -s /home/steam/steamcmd/linux32/steamclient.so
/home/steam/.steam/sdk32/steamclient.so && \  
chown -R steam /home/steam && \  
chown -R steam /configuration && \  
chown -R steam /data  
  
USER steam  
  
VOLUME ["/configuration", "/data"]  
  
COPY ./install.sh ./install.sh  
  
ENTRYPOINT ./install.sh && /configuration/startup.sh  

