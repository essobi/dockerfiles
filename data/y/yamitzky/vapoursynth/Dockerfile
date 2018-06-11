FROM ubuntu:16.04  
RUN apt-get update -y --fix-missing && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:djcj/vapoursynth && \  
apt-get update -y --fix-missing && \  
apt-get install -y \  
vapoursynth \  
vapoursynth-extra-plugins  
  
WORKDIR /data  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["vspipe"]  

