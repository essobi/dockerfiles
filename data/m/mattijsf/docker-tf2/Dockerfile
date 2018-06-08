FROM ubuntu:14.04  
# Set up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates lib32gcc1
lib32tinfo5 wget curl && \  
useradd -ms /bin/bash steam  
  
WORKDIR /home/steam  
  
USER steam  
  
RUN curl -sqL
'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar
zxvf - && \  
./steamcmd.sh +login anonymous +force_install_dir /home/steam/tf2 +app_update
232250 validate +quit && \  
mkdir -p .steam/sdk32 && \  
ln -s /home/steam/linux32/* /home/steam/.steam/sdk32  
  
# Make server port available to host  
EXPOSE 27015:27015  
EXPOSE 27015:27015/udp  
EXPOSE 27005:27005  
EXPOSE 27005:27005/udp  
EXPOSE 1200:1200  
EXPOSE 1200:1200/udp  
  
WORKDIR /home/steam/tf2  
ENTRYPOINT ["./srcds_run"]  
CMD ["+sv_lan 1 -game tf -port 27015 +map plr_pipeline +maxplayers 24 -ip
0.0.0.0"]

