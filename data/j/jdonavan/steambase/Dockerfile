FROM debian:jessie  
MAINTAINER Donavan Stanley <donavan.stanley@gmail.com>  
  
RUN mkdir -p /opt/steam/servers  
  
VOLUME ["/opt/steam/save"]  
VOLUME ["/opt/steam/workshop"]  
VOLUME ["/opt/steam/mods"]  
  
RUN apt-get update  
RUN apt-get install -y wget lib32stdc++6 ruby  
  
RUN useradd -ms /bin/bash steam  
  
# Install SteamCMD  
RUN mkdir /home/steam/steamcmd  
WORKDIR /home/steam/steamcmd  
  
RUN echo 'foo' > /dev/null  
  
RUN wget
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz  
RUN tar -xvzf steamcmd_linux.tar.gz  
RUN rm steamcmd_linux.tar.gz  
  
RUN chown -R steam:steam /home/steam/steamcmd  
RUN chown -R steam:steam /opt/steam  
  
# Install our helper tools  
ADD install_steam_app /usr/local/bin/install_steam_app  
ADD install_steam_mod /usr/local/bin/install_steam_mod  
ADD extract_mod.sh /usr/local/bin/extract_mod.sh  
ADD update_all_mods /usr/local/bin/update_all_mods  
  
# Switch over to the steam user for the rest  
USER steam  
  
# Launch SteamCMD once because so it can update if needed  
RUN echo "foo"  
RUN /home/steam/steamcmd/steamcmd.sh +login anonymous +quit  
RUN mkdir -p /home/steam/steamcmd/steamapps  
RUN ln -s /opt/steam/workshop /home/steam/steamcmd/steamapps/workshop  

