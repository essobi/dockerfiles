FROM ubuntu:xenial  
  
RUN apt-get update &&\  
apt-get install -y \  
wget \  
libcurl3 \  
libpng12-0 \  
libqt5core5a \  
libqt5gui5 \  
libqt5opengl5 \  
libqt5widgets5 \  
libgl1 \  
psmisc \  
libxmu6 \  
libxinerama1 \  
libxcursor1 \  
libqt5printsupport5 \  
libqt5x11extras5 \  
libsdl1.2debian \  
libvpx3  
  
RUN wget
http://download.virtualbox.org/virtualbox/5.1.26/virtualbox-5.1_5.1.26-117224~Ubuntu~xenial_amd64.deb
&& \  
dpkg -i virtualbox* &&\  
rm -fr virtualbox*  
  
CMD virtualbox

