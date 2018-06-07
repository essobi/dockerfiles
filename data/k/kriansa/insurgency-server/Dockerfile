FROM kriansa/steamcmd:latest  
LABEL maintainer="Daniel Pereira <daniel@garajau.com.br>"  
LABEL repository="kriansa/insurgency-server"  
  
# Build-time settings  
ARG GAME_ID=237410  
# Runtime settings  
ENV RCON_PASSWORD=""  
ENV SV_PASSWORD=""  
ENV MAXPLAYERS="48"  
ENV MAPNAME="market_coop checkpoint"  
# Set the server path  
ENV SERVER_PATH=$HOME/server  
  
# Install game server  
RUN steamcmd +login anonymous \  
+force_install_dir $SERVER_PATH \  
+app_update $GAME_ID validate \  
+quit  
  
# Set our workdir  
WORKDIR $SERVER_PATH  
  
# Create the banned files to be used to store ban info  
RUN touch insurgency/cfg/servervoiceban.cfg insurgency/cfg/banned_user.cfg  
  
# Required step to run srcds  
ENV LD_LIBRARY_PATH="$SERVER_PATH:$SERVER_PATH/bin:${LD_LIBRARY_PATH}"  
# Expose ports  
EXPOSE 27015/tcp 27015/udp  
  
# Default run command  
CMD ./srcds_linux -port 27015 -ip 0.0.0.0 +map $MAPNAME \  
+maxplayers $MAXPLAYERS +rcon_password "$RCON_PASSWORD" \  
+sv_password "$SV_PASSWORD"  

