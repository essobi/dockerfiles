FROM ubuntu:16.04  
ENV KILLING_FLOOR_2_VERSION 1064  
RUN addgroup --gid 1000 steam && \  
adduser --disabled-password --disabled-login --gecos "" \--uid 1000 --gid 1000
steam  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y ca-certificates && \  
(echo 2 | apt-get install -y steamcmd) && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /config && chown steam:steam /config  
  
WORKDIR /home/steam  
USER steam  
  
RUN ln -s /usr/games/steamcmd steamcmd  
RUN ./steamcmd +login anonymous +force_install_dir /home/steam/kf2 +app_update
232130 +exit  
  
# Initialize all config files  
USER steam  
COPY init-config.sh .  
RUN ./init-config.sh  
  
ENTRYPOINT ["./kf2/Binaries/Win64/KFGameSteamServer.bin.x86_64", "kf-
bioticslab"]  
  

