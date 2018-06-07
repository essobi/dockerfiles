FROM ubuntu:16.04  
MAINTAINER Wouter Haffmans <wouter@simply-life.net>  
  
RUN apt-get update \  
&& apt-get install -y \  
software-properties-common \  
wget \  
curl  
  
RUN add-apt-repository -y ppa:george-edison55/cmake-3.x \  
&& apt-key update \  
&& apt-get update && apt-get install -y \  
build-essential \  
git  
  
RUN apt-get install -y \  
cmake \  
libqt5concurrent5 \  
libqt5core5a \  
libqt5dbus5 \  
libqt5declarative5 \  
libqt5gui5 \  
libqt5multimedia5 \  
libqt5network5 \  
libqt5opengl5 \  
libqt5opengl5-dev \  
libqt5qml-graphicaleffects \  
libqt5qml5 \  
libqt5quick5 \  
libqt5quicktest5 \  
libqt5script5 \  
libqt5scripttools5 \  
libqt5svg5 \  
libqt5svg5-dev \  
libqt5widgets5 \  
libqt5xml5 \  
pyqt5-dev \  
python3-pyqt5 \  
python3-pyqt5-dbg \  
qt5-default \  
qt5-qmake \  
qt5-image-formats-plugins \  
qtdeclarative5-controls-plugin \  
qtdeclarative5-dbg \  
qtdeclarative5-dev \  
qtdeclarative5-dev-tools \  
qtdeclarative5-dialogs-plugin \  
qtdeclarative5-models-plugin \  
qtdeclarative5-qtquick2-plugin \  
qtdeclarative5-window-plugin \  
qttools5-dev-tools \  
qttools5-dev  
  
RUN apt-get install -y \  
libncurses5 \  
libncurses5-dbg \  
libncurses5-dev \  
libncursesw5 \  
libncursesw5-dbg \  
libncursesw5-dev \  
libreadline6 \  
libreadline6-dev \  
libmagick++6 \  
libmagick++-dev \  
imagemagick  
  
# Create devel user...  
RUN useradd -m -d /home/devel -u 1000 -U -G users,tty -s /bin/bash devel  
USER devel  
ENV HOME=/home/devel  
WORKDIR /home/devel  
  
# ... but don't use it on the next image builds  
ONBUILD USER root  
ONBUILD WORKDIR /  

