########################################################################################################  
# TShock server runner (TShock v4.3.11 for Terraria v1.3.08).  
# Volume mount points:  
# /Server/ServerPlugins. - TShock server plugins (Optional).  
# /Wolrd - World files, config, logs, etc. (Better to hold in volume container
or host).  
########################################################################################################  
FROM debian:jessie  
  
# Mono to run TShock server  
RUN apt-get update && apt-get -y install wget unzip screen \  
libmono-corlib4.0-cil libmono-sqlite4.0-cil libmono-system-core4.0-cil
libmono-system-net4.0-cil \  
libmono-system-runtime4.0-cil mono-runtime mono-runtime-sgen libmono-
corlib4.0-cil \  
libmono-sqlite4.0-cil libmono-system-core4.0-cil libmono-system-net4.0-cil \  
libmono-system-runtime4.0-cil mono-runtime mono-runtime-sgen libmono-data-
tds4.0-cil \  
libmysql6.4-cil libmono-system-runtime-serialization4.0-cil \  
libmono-system-runtime-serialization-formatters-soap4.0-cil libmono-system-
data-linq4.0-cil \  
libmono-system-xml-linq4.0-cil libmono-system-xml-serialization4.0-cil
libmono-system-xml4.0-cil \  
libmono-system-numerics4.0-cil zip wget  
  
# User ID and group ID to set volume owner (Default 2000).  
ENV UID 2000  
ENV GID 2000  
  
# USER "runner" with uid "2000" to run server.  
RUN groupadd -g $GID runner && useradd -g runner runner -u $UID  
  
# TShock version.  
ENV TSHOCK_VERSION 4.3.11  
# Server location.  
RUN mkdir /Server && chown $UID:$GID /Server  
WORKDIR /Server  
# World files.  
RUN mkdir /World && chown $UID:$GID /World  
  
# Run as USER.  
USER runner  
# Download TShock.  
RUN wget -c
https://github.com/NyxStudios/TShock/releases/download/v$TSHOCK_VERSION/tshock_release.zip
&& unzip tshock_release.zip -d /Server && rm tshock_release.zip  
  
# TShock server port.  
EXPOSE 7777  
VOLUME ["/World"]  
  
# Start server.  
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe"]  
CMD ["-configpath", "/World", "-worldpath", "/World", "-logpath", "/World"]  

