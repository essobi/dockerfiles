FROM zobees/mvdsv  
MAINTAINER cliffrowley@gmail.com  
  
ENV QW_MOUNT=/qw-mount \  
PORT=27500 \  
QW_NAME="QuakeWorld Server" \  
QW_ADMIN="Nobody" \  
QW_URL="" \  
QW_GAMENAME="qw" \  
QW_PASSWORD="" \  
QW_RCON_PASSWORD="" \  
QW_ADMIN_PASSWORD="" \  
QW_MAX_CLIENTS=16 \  
QW_MAX_SPECTATORS=2 \  
QW_TIMELIMIT=35 \  
QW_FRAGLIMIT=150 \  
QW_MAP="dm3" \  
QW_MAPLIST=""  
ADD files/qw/ $QW_DIR  
  
EXPOSE $PORT  
  
VOLUME $QW_MOUNT  
  
CMD $QW_DIR/run.sh

