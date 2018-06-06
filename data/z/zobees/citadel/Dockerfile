FROM zobees/steamcmd  
MAINTAINER cliffrowley@gmail.com  
  
USER root  
  
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get install -y
xdg-utils  
  
ENV STEAM_APP_ID="489650" \  
STEAM_APP_ANONYMOUS="1" \  
CITADEL_DIR="/citadel"  
  
COPY files/server.sh /server.sh  
  
RUN useradd -ms /bin/bash citadel  
  
RUN mkdir -p $CITADEL_DIR && \  
chmod 755 /server.sh && \  
chown -R citadel:citadel /home/steam && \  
chmod +x /home/steam/Steam/steamcmd.sh && \  
chmod +x /home/steam/Steam/linux32/steamcmd  
  
WORKDIR $CITADEL_DIR  
  
USER citadel  
  
VOLUME $CITADEL_DIR  
  
CMD /server.sh  

