FROM ubuntu:latest  
ADD ./files/supervisor.sh /  
RUN apt-get update \  
&& apt-get install -y wget lib32gcc1 lib32tinfo5 unzip \  
&& wget -O /tmp/steamcmd_linux.tar.gz
http://media.steampowered.com/installer/steamcmd_linux.tar.gz \  
&& mkdir -p /opt/steam \  
&& tar -C /opt/steam -xvzf /tmp/steamcmd_linux.tar.gz \  
&& rm /tmp/steamcmd_linux.tar.gz \  
&& mkdir -p /opt/steam/css \  
&& opt/steam/steamcmd.sh +login anonymous +force_install_dir /opt/steam/css/
+app_update 232330 validate +quit \  
&& chmod +x /supervisor.sh \  
&& apt-get remove -y unzip \  
&& useradd -ms /bin/bash steam \  
&& chown -R steam:steam /opt/steam/css  
ADD ./files/cfg/ /opt/steam/css/cstrike/cfg  
ENV CSS_HOSTNAME Counter-Strike Source Dedicated Server  
ENV CSS_PASSWORD ""  
ENV RCON_PASSWORD somepassword  
EXPOSE 27015/udp  
EXPOSE 27015  
EXPOSE 1200  
EXPOSE 27005/udp  
EXPOSE 27020/udp  
EXPOSE 26901/udp  
VOLUME ["/opt/steam/css/cstrike/cfg"]  
USER steam  
CMD ["/supervisor.sh"]

