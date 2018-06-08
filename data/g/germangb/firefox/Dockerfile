#  
# docker run \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/.firefox/mozilla:/home/firefox/.mozilla \  
# -v $HOME/.firefox/cache:/home/firefox/.cache \  
# -v $HOME/Downloads:/home/firefox/Downloads \  
# -e DISPLAY=$DISPLAY \  
# --name firefox \  
# --device /dev/snd \  
# --device /dev/dri \  
# germangb/firefox "$@"  
#  
FROM ubuntu:trusty  
MAINTAINER @germangb <germangb42@gmail.com>  
  
ARG uid=1000  
ARG gid=1000  
RUN groupadd -g ${gid} firefox && \  
useradd -g ${gid} -u ${uid} -m firefox  
  
RUN apt-get update && apt-get install -y \  
libgl1-mesa-dev \  
firefox \  
&& rm -rf /var/lib/apt/lists/*  
  
USER firefox  
  
WORKDIR /home/firefox  
  
ENTRYPOINT ["firefox"]  

