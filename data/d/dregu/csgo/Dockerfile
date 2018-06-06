FROM phusion/baseimage:0.9.18  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  
EXPOSE 27020/udp  
EXPOSE 27005/udp  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
CMD bash  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
lib32gcc1 libstdc++6:i386 curl tmux bsdmainutils wget mailutils postfix git
nano unzip binutils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* \  
&& (useradd -m cs && chown cs:cs /home/cs -R && echo "cs ALL=(ALL)
NOPASSWD:ALL" >> /etc/sudoers) \  
&& (echo "cs ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers)  
USER cs  
WORKDIR /home/cs  
RUN wget -N --no-check-certificate
https://gameservermanagers.com/dl/linuxgsm.sh && chmod +x linuxgsm.sh && bash
linuxgsm.sh csgoserver  
RUN ./csgoserver auto-install  
RUN (echo '#!/bin/bash\n \  
sed -i "/hostname \"/s/\"\\([^\\\"]*\\)\"/\"$HOSTNAME\"/"
serverfiles/csgo/cfg/csgo-server.cfg\n \  
sed -i "/rcon_password \"/s/\"\\([^\\\"]*\\)\"/\"$RCONPASSWORD\"/"
serverfiles/csgo/cfg/csgo-server.cfg\n \  
sed -i "/sv_password \"/s/\"\\([^\\\"]*\\)\"/\"$PASSWORD\"/"
serverfiles/csgo/cfg/csgo-server.cfg\n \  
cd /home/cs/serverfiles\n \  
./srcds_run -game csgo -usercon -strictportbind -ip $(hostname --ip-address)
-port 27015 +clientport 27005 +tv_port 27020 -tickrate $TICKRATE
+sv_setsteamaccount $GSLT +map $MAP +servercfgfile \  
csgo-server.cfg -maxplayers_override $MAXPLAYERS +mapgroup $MAPGROUP
+game_mode $GAMEMODE +game_type $GAMETYPE +net_public_adr $PUBLIC $CUSTOM' >>
/home/cs/start) \  
&& chmod a+x /home/cs/start && mkdir -p /home/cs/serverfiles/csgo/matches &&
(sudo sh -c "echo Europe/Helsinki > /etc/timezone") && sudo dpkg-reconfigure
-f noninteractive tzdata  
COPY esl5on5.cfg /home/cs/serverfiles/csgo/cfg/esl5on5.cfg  
COPY aim_map.bsp /home/cs/serverfiles/csgo/maps/aim_map.bsp  
VOLUME /home/cs/serverfiles/csgo/matches  

