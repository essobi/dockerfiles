FROM ubuntu:14.04  
# Set up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates lib32gcc1
lib32tinfo5 wget curl && \  
useradd -ms /bin/bash steam  
  
RUN ln -s /home/steam/css/cstrike/cfg /config && chown -R steam:steam /config  
  
WORKDIR /home/steam  
  
USER steam  
  
RUN curl -sqL
'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar
zxvf - && \  
./steamcmd.sh +login anonymous +force_install_dir /home/steam/css +app_update
232330 validate +quit && \  
mkdir -p .steam/sdk32 && \  
ln -s /home/steam/linux32 .steam/sdk32  
  
# Make server port available to host  
EXPOSE 27015/udp  
EXPOSE 27015  
EXPOSE 1200  
EXPOSE 27005/udp  
EXPOSE 27020/udp  
EXPOSE 26901/udp  
  
WORKDIR /home/steam/css  
ENTRYPOINT ["./srcds_run"]  
CMD ["+sv_lan 1 -game cstrike -port 27015 +map de_dust +maxplayers 20 -ip
0.0.0.0 -nobreakpad"]  

