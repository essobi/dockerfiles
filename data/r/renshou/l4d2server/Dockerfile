FROM renshou/steamcmd:latest  
  
# Prevent some warnings  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Default port binding  
ENV BIND_PORT=27015  
ENV BIND_IP=0.0.0.0  
  
# SRCDS parameters  
ENV SRCDS_GAME=left4dead2  
ENV SRCDS_HOSTNAME="Speranza's L4D2"  
# Copy scripts  
COPY ./scripts/ /usr/games/gameserver/  
  
# Copy cfg callback  
COPY server.cfg /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server.cfg  
  
# Create forward mount symlinks  
RUN mkdir -p /mnt/srcds \  
&& ln -s /usr/games/gameserver/serverfiles/${SRCDS_GAME}/addons
/mnt/srcds/addons \  
&& ln -s /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/sourcemod
/mnt/srcds/cfg-sourcemod \  
&& ln -s /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server
/mnt/srcds/cfg-server \  
# Create reverse mount symlinks  
&& mkdir -p /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg \  
&& ln -s /usr/games/gameserver/mods/cfg/sourcemod
/usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/sourcemod \  
&& ln -s /usr/games/gameserver/mods/addons
/usr/games/gameserver/serverfiles/${SRCDS_GAME}/addons \  
&& ln -s /usr/games/gameserver/mods/cfg/server
/usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server \  
# Create user customization folders  
&& mkdir -p /usr/games/gameserver/mods/cfg/sourcemod
/usr/games/gameserver/mods/addons /usr/games/gameserver/mods/cfg/server \  
# Change permissions  
&& chown -R gameserver:gameserver /usr/games/gameserver \  
&& chmod +x /usr/games/gameserver/start.sh  
  
# Switch to non root user  
USER gameserver  
  
CMD ["+map c5m1_waterfront"]

