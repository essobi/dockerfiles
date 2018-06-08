#  
# docker run \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/Pictures:/home/gimp/Pictures \  
# -e DISPLAY=$DISPLAY \  
# --name gimp \  
# --device /dev/dri \  
# germangb/gimp "$@"  
#  
FROM ubuntu:trusty  
MAINTAINER @germangb <germangb42@gmail.com>  
  
ARG uid=1000  
RUN useradd -m -u ${uid} -m gimp  
  
RUN apt-get update && apt-get install -y \  
libgl1-mesa-dev \  
gimp \  
&& rm -rf /var/lib/apt/lists/*  
  
user gimp  
  
WORKDIR /home/gimp  
  
ENTRYPOINT ["gimp"]  

