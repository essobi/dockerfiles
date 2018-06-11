FROM debian:wheezy  
MAINTAINER troyswanson <gerphimum@gmail.com>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
lib32gcc1  
  
RUN useradd -m steam  
  
USER steam  
  
ENV GAME_TYPE 0  
ENV GAME_MODE 1  
ENV MAP_GROUP mg_active  
ENV START_MAP de_dust2  
  
WORKDIR /var/lib/steam  
  
CMD ./srcds_run \  
-game csgo \  
-console \  
+game_type $GAME_TYPE \  
+game_mode $GAME_MODE \  
+mapgroup $MAP_GROUP \  
+map $START_MAP  
  
EXPOSE 27015  

