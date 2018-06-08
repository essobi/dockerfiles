FROM frostasm/qt:qt5.9.3-desktop-qtav-qjsonserializer  
MAINTAINER frostasm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY install-linuxdeployqt.sh /tmp/qt/  
  
RUN sudo apt-get install  
  
RUN sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends \  
libxi6 libgconf-2-4 libgtk-3-0 libx11-xcb1 libpq5 &&\  
sudo apt-get -qq clean  
  
RUN cd /tmp/qt/ && \  
sudo /tmp/qt/install-linuxdeployqt.sh && \  
sudo rm -rf /tmp/qt

