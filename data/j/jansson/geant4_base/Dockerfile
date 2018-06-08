FROM jansson/dev  
  
# Installing stuff to be able to use Geant4 visualization.  
# Prevent interactivity.  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
freeglut3-dev \  
libmotif-dev \  
xorg \  
xorg-dev \  
&& rm -rf /var/lib/apt/lists/* /core  
  
ENV GEANT4_VERSION 10.04.p02  

