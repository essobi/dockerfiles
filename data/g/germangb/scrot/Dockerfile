#  
# docker run \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/Pictures:/home/scrot \  
# -e DISPLAY=$DISPLAY \  
# germangb/scrot "$@"  
#  
FROM ubuntu:trusty  
MAINTAINER @germangb <germangb42@gmail.com>  
  
ARG uid=1000  
ARG gid=1000  
RUN groupadd -g ${gid} scrot && \  
useradd -g ${gid} -u ${uid} -m scrot  
  
RUN apt-get update && apt-get install -y scrot \  
&& rm -rf /var/lib/apt/lists/*  
  
USER scrot  
  
WORKDIR /home/scrot  
  
ENTRYPOINT ["scrot"]  

