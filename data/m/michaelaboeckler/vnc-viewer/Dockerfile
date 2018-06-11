FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get update && apt-get install -y \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
vncviewer \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
#change User to run vnc  
ENV HOME /home/vnc  
RUN useradd -m vnc  
  
WORKDIR $HOME  
USER vnc  
ENTRYPOINT ["vncviewer"]

