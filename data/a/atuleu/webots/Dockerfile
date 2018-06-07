FROM biorob/base:v1  
MAINTAINER Alexandre Tuleu <alexandre.tuleu@polytechnique.org>  
RUN wget -q http://www.cyberbotics.com/archive/linux/webots_6.4.4_$(dpkg
--print-architecture).deb  
RUN apt-get update && apt-get install -y \  
libglu1-mesa \  
libjpeg62 \  
libpango1.0-0 \  
libgtk2.0-0 \  
xdg-utils \  
mesa-common-dev \  
libssl0.9.8  
  
RUN dpkg -i webots_6.4.4_$(dpkg --print-architecture).deb  
RUN rm webots_6.4.4_$(dpkg --print-architecture).deb  

