FROM debian:jessie-slim  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# Requirements  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free' >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -y install libx11-xcb1 libfontconfig1 libdbus-1-3 libgl1-mesa-glx
libglib2.0-0 libxkbcommon-dev \  
libxi6 libsm6 libice6 libxrender1 libegl1-mesa \  
wget git make gcc cmake-data=3.6.2-2~bpo8+1 cmake=3.6.2-2~bpo8+1 g++ libdrm-
dev \  
libqt5quickwidgets5 libfontconfig1-dev \  
freeglut3-dev \  
libnss3 libasound2 libxtst6 libxslt1.1 \  
&& wget download.qt.io/official_releases/qt/5.6/5.6.2/qt-opensource-
linux-x64-5.6.2.run \  
&& git clone \--recurse-submodules https://github.com/hteso/iaito.git  
  
WORKDIR /iaito/radare2/  
RUN ./sys/install.sh \  
&& chmod +x /qt-opensource-linux-x64-5.6.2.run  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

