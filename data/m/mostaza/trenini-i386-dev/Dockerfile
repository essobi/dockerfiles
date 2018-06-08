FROM ioft/i386-ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
# update system  
RUN apt-get -y update && apt-get -y upgrade  
  
# build tools  
RUN apt-get -y --no-install-recommends install build-essential yasm  
RUN apt-get -y --no-install-recommends install fakeroot  
RUN apt-get -y --no-install-recommends install curl ca-certificates  
RUN apt-get -y --no-install-recommends install git  
RUN apt-get -y --no-install-recommends install libmysqlclient-dev libtinyxml-
dev libsqlite3-dev  
  
# build deps  
# build deps - ffmpeg  
RUN curl https://ffmpeg.org/releases/ffmpeg-2.2.16.tar.gz | tar xz  
WORKDIR ffmpeg-2.2.16  
RUN ls -la  
RUN ./configure && make && make install  
WORKDIR /  
  
# build deps - zlib  
RUN apt-get -y --no-install-recommends install libz-dev  
# build deps - libcurl  
RUN apt-get -y --no-install-recommends install libcurl3-gnutls-dev  
# build deps - log4cpp  
RUN apt-get -y --no-install-recommends install liblog4cpp5-dev  
  
# build deps - boost  
RUN apt-get -y --no-install-recommends install \  
libboost-thread-dev \  
libboost-chrono-dev \  
libboost-system-dev  
  
# build deps - Qt  
RUN apt-get -y --no-install-recommends install \  
qtmobility-dev \  
libqt4-dev  

