FROM rbwsam/steamcmd:latest  
RUN ./steamcmd.sh +login anonymous +force_install_dir /home/steam/dods
+app_update 232290 validate +quit  
WORKDIR /home/steam/dods  
RUN echo "rcon_password \"password\"" > dod/cfg/server.cfg  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

