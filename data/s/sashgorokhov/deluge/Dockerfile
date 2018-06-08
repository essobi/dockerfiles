FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y deluged deluge-web  
  
ENV LOGLEVEL=info \  
BASE="/" \  
PORT=8112 \  
DAEMON_PORT=58846  
  
EXPOSE $PORT $DAEMON_PORT  
VOLUME /media  
  
RUN deluged -p $DAEMON_PORT  
CMD deluge-web -L $LOGLEVEL -b $BASE -p $PORT  

