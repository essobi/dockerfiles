FROM brettowen/tf2-docker-base  
  
MAINTAINER Brett Owen <brett@brettowen.ca>  
  
WORKDIR /home/steam/steamcmd/tf2/tf  
RUN wget
https://mms.alliedmods.net/mmsdrop/1.10/mmsource-1.10.7-git961-linux.tar.gz  
RUN wget
https://sm.alliedmods.net/smdrop/1.8/sourcemod-1.8.0-git6040-linux.tar.gz  
  
RUN tar -xvzf mmsource-1.10.7-git961-linux.tar.gz  
RUN tar -xvzf sourcemod-1.8.0-git6040-linux.tar.gz  
ADD metamod.vdf /home/steam/steamcmd/tf2/tf/addons/metamod.vdf  
  
ADD ./install/tf /mnt/  
RUN cp -af /mnt/* /home/steam/steamcmd/tf2/tf  
  
ADD startserver.sh /home/steam/steamcmd/startserver.sh  
  
ENV MAP="ctf_ballin_skyfall"  
ENV SV_MAXPLAYERS=15  
ENV SV_HOSTNAME="changeme"  
ENV RCON_PASSWORD="changeme"  
ENV SV_PORT=27015  
ENV LOGS_APIKEY=0  
ENV DEMOS_APIKEY=0  
EXPOSE 27015 27015/udp  
  
ENTRYPOINT ["/home/steam/steamcmd/startserver.sh"]  

