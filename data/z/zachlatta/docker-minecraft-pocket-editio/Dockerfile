FROM ubuntu  
MAINTAINER Zach Latta <zach@zachlatta.com>  
  
RUN apt-get update  
RUN apt-get install -y make autoconf automake libtool m4 wget  
  
RUN useradd -s /bin/bash -d /minecraft -m minecraft  
  
ADD https://github.com/PocketMine/PocketMine-
MP/releases/download/Alpha_1.3.9/PocketMine-MP_Installer_Alpha_1.3.9.sh
/minecraft/install.sh  
RUN cd /minecraft && sh install.sh  
RUN chown -R minecraft:minecraft /minecraft  
  
USER minecraft  
WORKDIR /minecraft  
VOLUME /minecraft  
EXPOSE 19132  
ENTRYPOINT ./start.sh  

