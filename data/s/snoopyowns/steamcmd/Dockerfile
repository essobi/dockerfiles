FROM ubuntu  
  
LABEL maintainer="Snoopyowns"  
  
RUN apt-get update  
RUN apt-get -y install lib32gcc1 libc6-i386 lib32stdc++6 wget  
  
ENV STEAM_DIR="/steam"  
ENV GAME_DIR="/game"  
RUN mkdir ${STEAM_DIR}  
RUN mkdir ${GAME_DIR}  
  
RUN cd ${STEAM_DIR}  
RUN wget -q -O ${STEAM_DIR}/steamcmd_linux.tar.gz
http://media.steampowered.com/client/steamcmd_linux.tar.gz  
RUN tar --directory ${STEAM_DIR} -xvzf /${STEAM_DIR}/steamcmd_linux.tar.gz  
RUN rm ${STEAM_DIR}/steamcmd_linux.tar.gz  
RUN chmod -R 774 ${STEAM_DIR}  
  
RUN ln -s /usr/games/steamcmd ${STEAM_DIR}  
  
RUN ${STEAM_DIR}/steamcmd.sh +login anonymous +quit  
  
RUN ulimit -n 2048  
  
ADD /scripts/ /opt/scripts/  
RUN chmod -R 774 /opt/scripts/  
  
ENTRYPOINT ["/opt/scripts/start-server.sh"]

