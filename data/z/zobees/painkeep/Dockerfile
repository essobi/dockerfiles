FROM zobees/quakeworld  
MAINTAINER cliffrowley@gmail.com  
  
ENV QW_NAME="PainKeep Server" \  
QW_GAMENAME="painkeep" \  
QW_MAX_CLIENTS=8 \  
QW_TIMELIMIT=25 \  
QW_FRAGLIMIT=75 \  
QW_MAP="start"  
ADD files/qw/painkeep $QW_DIR/painkeep  
ADD files/qw/templates/painkeep/server.cfg
$QW_DIR/templates/painkeep/server.cfg  

