# start with a micro image  
FROM accursoft/micro-debian:latest  
  
# environment variables  
ENV STEAMCMD /steamcmd  
ENV PATH $STEAMCMD:$PATH  
ENV CONFIG /config  
ENV PATH $CONFIG:$PATH  
ENV SCRIPT jc2.config  
ENV INIT start-jc2.sh  
ENV USERNAME anonymous  
ENV PASSWORD ""  
# ports  
# 7777 => game port, 27015 => query port, 20560 => steam  
EXPOSE 7777 27015 20560  
# set our working directory to steamcmd  
WORKDIR /steamcmd  
  
# make a directory for our server scripts  
RUN mkdir /config  
  
# copy our server and config file to /config  
COPY config/ $CONFIG  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y lib32gcc1 curl bash && \  
apt-get clean  
  
# download steamcmd and un-tar it  
RUN curl -sqL
'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar
zxvf -  
  
# copy our docker-entrypoint.sh script to /steamcmd  
COPY docker-entrypoint.sh $STEAMCMD  
  
# create a mount point for our config dir  
VOLUME ${CONFIG}  
  
# start steamcmd  
CMD ["bash", "-c", "./docker-entrypoint.sh"]  

