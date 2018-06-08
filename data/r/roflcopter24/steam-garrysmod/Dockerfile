# Dockerfile for Garry's Mod server  
FROM debian  
  
LABEL maintainer=florian@eagle-eye-studios.net  
LABEL version=2017.04.20  
  
# Enable 32-bit packages and update pkg cache  
RUN dpkg --add-architecture i386 && apt-get update  
  
# Install deps  
RUN apt-get install wget lib32gcc1 libc6:i386 libstdc++6:i386 -y  
  
# add user and group  
RUN addgroup steam && adduser -q --no-create-home --disabled-password
--ingroup steam steam  
  
# Create install folder for game server  
RUN mkdir /srv/steam && chown -R steam:steam /srv/steam  
  
# create directory structure  
RUN cd /srv/steam && su steam && mkdir content gmodds Steam content/css  
  
# Get Steam cmd launcher  
RUN su steam && cd /srv/steam/Steam && wget
http://media.steampowered.com/client/steamcmd_linux.tar.gz && tar -xvzf
steamcmd_linux.tar.gz  
  
# Make sure rights are correct  
RUN su steam && chown -R steam:steam /srv/steam && chmod a+x
/srv/steam/Steam/steamcmd.sh  
  
# Update steam  
RUN cd /srv/steam/Steam && su -c '/srv/steam/Steam/steamcmd.sh +login
anonymous +quit' steam  
  
# Download Garry's mod  
RUN cd /srv/steam/Steam && su -c '/srv/steam/Steam/steamcmd.sh +login
anonymous +force_install_dir "/srv/steam/gmodds" +app_update 4020 validate
+quit' steam  
  
# Donwload Counter Strike Source files  
RUN su steam && cd /srv/steam/Steam && /srv/steam/Steam/steamcmd.sh
+force_install_dir "/srv/steam/content/css" +login anonymous +app_update
232330 +quit  
  
# Add mount config so GMod can find CSS files  
RUN su steam && printf '"mountcfg"\n{\n"cstrike"
"/srv/steam/content/css/cstrike"\n}\n' >>
/srv/steam/gmodds/garrysmod/cfg/mount.cfg  
  
# Expose configuration folder of Garry's Mod  
VOLUME /srv/steam/gmodds/garrysmod/cfg  
VOLUME /srv/steam/gmodds/garrysmod/addons  
  
# Copy run script from build context  
ADD run.sh /usr/bin/run.sh  
  
# Set run script to executable  
RUN chmod a+x /usr/bin/run.sh  
  
# Set environment variables so Plaer count, startup map and game mode can
easily be changed  
# by the 'docker run' command  
ENV MAX_PLAYERS=16  
ENV START_MAP=gm_construct  
ENV GAME_MODE=terrortown  
ENV STEAM_API_KEY=xxxx  
ENV STEAM_WS_COLL=xxxx  
  
EXPOSE 27005 27015  
# Entrypoint  
ENTRYPOINT ["run.sh"]  

