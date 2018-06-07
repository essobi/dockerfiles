FROM debian:stretch  
WORKDIR /var/maniaplanet  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
unzip \  
libc6  
  
#  
# Download the dedicated server.  
#  
RUN wget http://files.v04.maniaplanet.com/server/ManiaplanetServer_Latest.zip
-qO /tmp/mpdedi.zip  
RUN unzip -quo /tmp/mpdedi.zip -d .  
RUN rm /tmp/mpdedi.zip  
RUN rm *.exe  
  
#  
# Copy de default dedicated config file  
#  
COPY ./default.config.xml /var/maniaplanet/UserData/Config/default.config.xml  
  
#  
# Copy custom script to launch the dedicated.  
#  
COPY ./run.sh /var/maniaplanet/  
RUN chmod +x run.sh  
  
#  
# Volumes not to loose data.  
#  
VOLUME /var/maniaplanet/UserData/Maps  
VOLUME /var/maniaplanet/UserData/Config  
VOLUME /var/maniaplanet/UserData/Scripts  
VOLUME /var/maniaplanet/Logs  
  
# game | p2p | xml-rpc  
EXPOSE 2350 2350/udp 3450 3450/udp 5000  
ENTRYPOINT ["./run.sh"]

