FROM renshou/steamcmd:latest  
# Prevent some warnings  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Default port binding  
ENV BIND_PORT=27015  
ENV BIND_IP=  
  
# SRCDS parameters  
ENV SRCDS_GAME=garrysmod  
ENV SRCDS_HOSTNAME="Speranza's Mod"  
# Copy scripts  
COPY ./scripts/ /usr/games/gameserver/  
# Copy cfg callback  
COPY server.cfg /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server.cfg  
# Install dependencies  
RUN apt-get update \  
&& apt-get -y install lib32ncurses5 \  
&& rm -rf /var/lib/apt/lists/* \  
# Create forward mount symlinks  
&& mkdir -p /mnt/srcds \  
&& ln -s /usr/games/gameserver/serverfiles/${SRCDS_GAME}/addons
/mnt/srcds/addons \  
&& ln -s /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server
/mnt/srcds/cfg-server \  
# Create reverse mount symlinks  
&& mkdir -p /usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg \  
&& ln -s /usr/games/gameserver/mods/addons
/usr/games/gameserver/serverfiles/${SRCDS_GAME}/addons \  
&& ln -s /usr/games/gameserver/mods/cfg/server
/usr/games/gameserver/serverfiles/${SRCDS_GAME}/cfg/server \  
# Create user customization folders  
&& mkdir -p /usr/games/gameserver/mods/addons
/usr/games/gameserver/mods/cfg/server \  
# Change permissions  
&& chown -R gameserver:gameserver /usr/games/gameserver \  
&& chmod +x /usr/games/gameserver/start.sh  
# Switch to non root user  
USER gameserver  
  
CMD ["+map gm_construct", "+gamemode sandbox"]

