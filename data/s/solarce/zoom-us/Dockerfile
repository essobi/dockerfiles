# Dockerfile to install the Zoom.us client on Ubuntu Trusty  
FROM ubuntu:trusty  
MAINTAINER Brandon Burton <brandon@inatree.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# enable i386 arch  
RUN sudo dpkg --add-architecture i386  
  
# refresh package lists  
RUN sudo apt-get update  
  
# Need curl to download the client .deb  
RUN sudo apt-get install curl -y  
  
# Dependencies for the client .deb  
RUN sudo apt-get install libglib2.0-0:i386 \  
libegl1-mesa:i386 libxcb-shape0:i386 \  
libxcb-shm0:i386 libgl1-mesa-glx:i386 \  
libxi6:i386 libsm6:i386 libfontconfig1:i386 \  
libxrender1:i386 libpulse0:i386 \  
libxcomposite1:i386 libxslt1.1:i386 \  
libgstreamer-plugins-base0.10-0:i386 \  
libssl1.0.0:i386 libxcb-randr0:i386 \  
libsqlite3-0:i386 desktop-file-utils -y  
  
# Grab the client .deb  
RUN curl -sSL https://zoom.us/client/latest/ZoomInstaller_i386.deb \  
-o /tmp/ZoomInstaller_i386.deb  
  
# Install the client .deb  
RUN sudo dpkg -i /tmp/ZoomInstaller_i386.deb  
  
# Some cleanup  
RUN sudo apt-get -f install  
  
CMD "/usr/bin/zoom"  
  

