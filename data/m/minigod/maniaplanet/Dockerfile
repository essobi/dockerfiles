# ManiaPlanet 3 Beta Server  
#  
# Version 2015.06.16 (2015-06-16)  
FROM debian:wheezy  
MAINTAINER Kristjan Broder Lund (MiniGod) <kristjan@lund.is>  
WORKDIR /maniaplanet  
  
# Dependencies  
RUN apt-get update -qq \  
&& apt-get install -yqq unzip wget \  
&& apt-get -yqq clean  
  
# Download and unzip  
#  
# Topic with all versions  
# https://forum.maniaplanet.com/viewtopic.php?f=261&t=12494  
RUN wget
http://files.maniaplanet.com/ManiaPlanet3Beta/ManiaPlanetBetaServer_2015-06-16.zip
-qO /tmp/mps.zip \  
&& unzip -quo /tmp/mps.zip -d . \  
&& rm /tmp/mps.zip \  
&& rm -rf *.bat *.exe *.html RemoteControlExamples/  
  
# Copy the default dedicated_cfg file  
COPY ./config.default.xml /maniaplanet/UserData/Config/config.xml  
  
# Need a custom script to start it up to be able to run multiple servers at
the same time (port issues)  
# This is better explained inside runner.sh  
COPY ./runner.sh /maniaplanet/  
RUN chmod +x /maniaplanet/runner.sh  
  
# Setup  
VOLUME /maniaplanet/UserData/  
VOLUME /maniaplanet/Logs/  
  
# game | p2p | xml-rpc  
EXPOSE 2350 2350/udp 3450 3450/udp 5000  
ENTRYPOINT ["./runner.sh"]  

