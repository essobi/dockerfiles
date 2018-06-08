from ubuntu:xenial  
  
MAINTAINER Brett Owen <brett@brettowen.ca>  
  
RUN dpkg --add-architecture i386  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y lib32z1 lib32ncurses5 lib32gcc1 lib32stdc++6 wget curl
libcurl3-gnutls:i386  
  
RUN useradd -m steam  
  
USER steam  
  
RUN mkdir /home/steam/steamcmd  
  
WORKDIR /home/steam/steamcmd  
RUN wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz  
RUN tar -xvzf steamcmd_linux.tar.gz  
  
ADD tf2serv.txt /home/steam/steamcmd/tf2serv.txt  
RUN /home/steam/steamcmd/steamcmd.sh +runscript
/home/steam/steamcmd/tf2serv.txt  
ADD startserver.sh /home/steam/steamcmd/startserver.sh  
  
ENV MAP="cp_badlands"  
ENV SV_MAXPLAYERS=12  
ENV RCON_PASSWORD="changeme"  
ENV SV_PORT=27015  
EXPOSE 27015 27015/udp  
  
ENTRYPOINT ["/home/steam/steamcmd/startserver.sh"]  

