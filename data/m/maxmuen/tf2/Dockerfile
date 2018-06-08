FROM i386/debian:testing-slim  
MAINTAINER github@maxmuen.de  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.build-date="2017-08-09T17:31:36+02:00" \  
org.label-schema.name="Team Fortress 2" \  
org.label-schema.description="Team Fortress 2 is a team-based first-person
shooter multiplayer video game developed and published by Valve Corporation."
\  
org.label-schema.url="http://www.teamfortress.com/" \  
org.label-schema.docker.cmd=" docker run --name tf2 -dt -v /opt/hlserver -v
/opt/tf2 -p 26901:26901/udp -p 27005:27005/udp -p 27015:27015/tcp -p
27015:27015/udp maxmuen/tf2:latest -nohltv +sv_setsteamaccount
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX +randommap +maxplayers 24"  
  
EXPOSE 26901/udp \  
27005/udp \  
27015/tcp \  
27015/udp  
  
COPY scripts/entrypoint /usr/local/bin/entrypoint  
  
RUN apt-get update && \  
apt-get upgrade --assume-yes && \  
apt-get install --assume-yes libcurl3-gnutls libz1 libncurses5 libstdc++6 curl
&& \  
mkdir -p /opt/tf2/tf/replay /opt/tf2/tf/custom /opt/tf2/tf/scripts
/opt/tf2/tf/materials /opt/tf2/tf/maps /opt/tf2/tf/cfg /opt/tf2/tf/workshop
/opt/tf2/.steam/sdk32 /opt/hlserver && \  
curl -sL http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
xzvf - -C /opt/hlserver && \  
apt-get purge --assume-yes curl && \  
apt-get autoremove --assume-yes && \  
apt-get clean --assume-yes && \  
rm -r /var/lib/apt/lists/*  
  
COPY maps /opt/tf2/tf/maps  
  
RUN adduser --system \--uid 50002 \--home /opt/tf2 --no-create-home
--disabled-login teamspeak && \  
chown teamspeak:nogroup -R /opt/tf2 /opt/hlserver  
  
USER teamspeak  
  
VOLUME ["/opt/hlserver", "/opt/tf2"]  
  
WORKDIR "/opt/tf2"  
ENTRYPOINT ["/usr/local/bin/entrypoint"]

