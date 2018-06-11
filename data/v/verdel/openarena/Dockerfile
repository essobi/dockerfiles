FROM progrium/busybox  
RUN opkg-install curl unzip  
  
#Install flexget and transmissionrpc  
RUN curl -o /tmp/openarena.zip
http://download.tuxfamily.org/openarena/rel/088/openarena-0.8.8.zip  
RUN mkdir -p /app  
RUN cd /tmp && unzip /tmp/openarena.zip -d /app && rm openarena.zip  
RUN rm -rf /tmp/* /var/tmp/*  
ADD server.cfg /app/openarena-0.8.8/baseoa/  
ADD private.cfg /app/openarena-0.8.8/baseoa/  
ADD maps/reqkitchen.pk3 /app/openarena-0.8.8/baseoa/  
ADD maps/reqbath.pk3 /app/openarena-0.8.8/baseoa/  
ADD maps/map-acid3dm9.pk3 /app/openarena-0.8.8/baseoa/  
ADD maps/woa.pk3 /app/openarena-0.8.8/baseoa/  
ADD maps/dum.pk3 /app/openarena-0.8.8/baseoa/  
  
EXPOSE 27960/udp  
EXPOSE 27950/udp  
  
#Run my_init  
CMD /app/openarena-0.8.8/oa_ded.x86_64 +set dedicated 1 +set sv_cheats 1 +exec
server.cfg  

