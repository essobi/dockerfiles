FROM thalhalla/steamer  
MAINTAINER Josh Cox <josh 'at' webhosting coop>  
  
ENV DOCKER7DAYSTODIE 2017012504  
# override these variables in with the prompts  
ENV STEAM_GID 294420  
ENV STEAM_FORCE_INSTALL /home/steam/7DaysToDie  
ENV STEAM_CMD_PATH /opt/steamer  
  
USER root  
# and override this file with the command to start your server  
COPY assets /assets  
RUN chmod 755 /assets/*.sh && \  
chmod 755 /assets/cfg/*.xml && \  
chmod 755 /assets/steamer.txt && \  
chown -R steam. /home/steam  
  
# Install frame buffer via non-interactive apt  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -yqq telnet xvfb libglu1-mesa libxcursor1 libxrandr2 && \  
rm -rf /var/lib/apt/lists/*  
# End non-interactive apt  
ENV DEBIAN_FRONTEND interactive  
  
USER steam  
WORKDIR /opt/steamer  
WORKDIR /home/steam  
  
CMD ["/bin/bash", "/assets/valve-start.sh"]  

