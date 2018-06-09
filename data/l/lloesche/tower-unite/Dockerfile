FROM debian:stable  
COPY supervisord.conf /etc/supervisor/conf.d/tower-unite.conf  
COPY tower-unite-server /usr/local/bin/  
COPY tower-unite-updater /usr/local/bin/  
ADD https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
/tmp  
RUN apt-get update \  
&& apt-get -y dist-upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
lib32gcc1 \  
ca-certificates \  
supervisor \  
procps \  
&& mkdir -p /var/log/supervisor /opt/tower-
unite/Tower/Saved/Config/LinuxServer /opt/steamcmd \  
&& apt-get clean \  
&& adduser \  
\--home /home/steam \  
\--disabled-password \  
\--shell /bin/bash \  
\--gecos "Steam User" \  
\--quiet \  
steam \  
&& cd /home/steam \  
&& tar xzvf /tmp/steamcmd_linux.tar.gz -C /opt/steamcmd/ \  
&& chown -R root:root /opt/steamcmd \  
&& chown steam:steam /opt/tower-unite/Tower/Saved/Config/LinuxServer \  
&& chmod 755 /opt/steamcmd/steamcmd.sh /opt/steamcmd/linux32/steamcmd
/opt/steamcmd/linux32/steamerrorreporter \  
&& chmod +x /usr/local/bin/tower-unite-* \  
&& cd "/opt/steamcmd" \  
&& ./steamcmd.sh +login anonymous +quit \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 27015-27050/udp 27015-27050/tcp 7777-7780/udp 3478/udp 4379-4380/udp  
WORKDIR /home/steam  
CMD ["/usr/bin/supervisord"]  

