FROM ubuntu:16.04  
MAINTAINER Stanley Förster <stanley.foerster@gmail.com>  
  
ENV USER user  
ENV HOME /home/${USER}  
ENV QT_MAJOR 5  
ENV QT_MINOR 8  
ENV QT_PATCH 0  
ENV QT_FIX ${QT_FIX}  
ENV QT_QPA_PLATFORM minimal  
ENV QT_DIR ${HOME}/qt  
ENV QT_INSTALLER qt-opensource-
linux-x64-${QT_MAJOR}.${QT_MINOR}.${QT_PATCH}${QT_FIX}.run  
ENV PATH ${PATH}:${QT_DIR}/${QT_MAJOR}.${QT_MINOR}/gcc_64/bin  
  
COPY setup.qs /tmp/  
  
RUN \  
apt-get -qq update && \  
apt-get -qq -y install \  
curl \  
git \  
build-essential \  
libgl1-mesa-dev \  
libfontconfig1-dev \  
libdbus-1-dev && \  
apt-get -qq clean  
  
RUN \  
curl -sL --retry 10 --retry-delay 10 -o /tmp/${QT_INSTALLER}
https://download.qt.io/official_releases/qt/${QT_MAJOR}.${QT_MINOR}/${QT_MAJOR}.${QT_MINOR}.${QT_PATCH}/${QT_INSTALLER}
&& \  
chmod +x /tmp/${QT_INSTALLER} && \  
/tmp/${QT_INSTALLER} \--no-force-installations --script /tmp/setup.qs && \  
rm -f /tmp/${QT_INSTALLER} /tmp/setup.qs  

