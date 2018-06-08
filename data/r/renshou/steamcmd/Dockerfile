FROM ubuntu:yakkety  
  
# Prevent some warnings  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Set entrypoint  
COPY entrypoint.sh /usr/games/gameserver/entrypoint.sh  
ENTRYPOINT ["/usr/games/gameserver/entrypoint.sh"]  
  
# Enable the multiverse source and install SteamCMD  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& echo steamcmd steam/question select I AGREE | debconf-set-selections \  
&& apt-get -y install ca-certificates steamcmd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# Add new user and assign ownership of entrypoint script  
&& adduser --disabled-password --gecos '' gameserver \  
&& chown gameserver:gameserver /usr/games/gameserver/entrypoint.sh \  
&& chmod +x /usr/games/gameserver/entrypoint.sh \  
# SteamInit crash fix  
&& mkdir -pv /home/gameserver/.steam/sdk32/ \  
&& ln -s /home/gameserver/.steam/steamcmd/linux32/steamclient.so
/home/gameserver/.steam/sdk32/steamclient.so  

