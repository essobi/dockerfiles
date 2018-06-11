# Usage:  
# export DISPLAY=:0  
# xhost +SI:localuser:root  
# docker run --rm -it \  
# -p 5900:5900 \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# --ipc=host -v /etc/localtime:/etc/localtime:ro  
# x11vnc  
  
FROM debian:latest  
  
RUN apt-get update && \  
apt-get install -y x11vnc --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/bin/x11vnc"]  

