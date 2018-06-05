FROM sfoxdev/steamcmd-rcon  
  
MAINTAINER SFoxDev <admin@sfoxdev.com>  
  
ENV LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
STEAMID="376030" \  
INSTALLDIR="/home/steam/ark/" \  
RCON_HOST="localhost" \  
RCON_PORT="32330" \  
RCON_PASSWORD="Gkjbha39skJ" \  
RCON_HEALTH_COMMAND="listplayers" \  
RCON_HEALTH_REGEXP="(No Players|[0-9]\\.)" \  
SERVER_NAME="ARK Server" \  
MAP_NAME="TheIsland" \  
MOD_LIST="" \  
DIFFICULTY="5.0" \  
MAX_PLAYERS="70" \  
BATTLE_EYE="false" \  
RCON_GAME_LOG_BUFFER="100" \  
WHITELIST_PLAYERS="" \  
ADDITIONAL_SERVER_COMMAND_LINE="" \  
AUTO_UPDATE="true" \  
SAVE_GAME_NAME="" \  
CLUSTER_NAME="" \  
PORT="7777" \  
RAWPORT="7778" \  
QUERYPORT="27015"  
# auto-fetch the rcon password from /home/steam/ark/rcon_pass  
USER root  
RUN sed -i 's|python|export RCON_PASSWORD=$(cat
/home/steam/ark/rcon_pass)\n&|' /home/steam/rcon/healthcheck.sh  
  
EXPOSE $PORT/udp $RAWPORT/udp $QUERYPORT/udp 32330  
WORKDIR /home/steam/ark/  
  
#ADD https://github.com/xcq1/ark-moddodo/archive/master.tar.gz
/home/steam/ark/  
ADD run.sh /home/steam/ark/run.sh  
ADD versioncheck /home/steam/ark/versioncheck  
ADD versioncheck/crontab /etc/cron.d/ark-cron  
  
RUN curl -Lo master.tar.gz https://github.com/xcq1/ark-
moddodo/archive/master.tar.gz \  
&& tar -xvzf /home/steam/ark/master.tar.gz \  
&& rm /home/steam/ark/master.tar.gz \  
&& chown -R steam:steam /home/steam/ark/ark-moddodo-master \  
&& chmod +x /home/steam/ark/run.sh \  
&& chown -R steam:steam /home/steam/ark \  
&& chmod +x /home/steam/ark/versioncheck/* \  
&& chmod +x /etc/cron.d/ark-cron \  
&& apt update \  
&& apt -y upgrade \  
&& apt install -y cron sudo python3 \  
&& apt clean \  
&& echo "steam ALL=NOPASSWD:ALL" >> /etc/sudoers  
  
VOLUME ["/home/steam"]  
  
STOPSIGNAL SIGINT  
  
USER steam  
  
CMD ["/home/steam/ark/run.sh"]  

