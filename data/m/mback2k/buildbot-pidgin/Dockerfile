FROM mback2k/buildbot:latest  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential automake autoconf intltool \  
make libtool-bin pkg-config curl wget unzip \  
binutils-mingw-w64 mingw-w64 mingw-w64-tools \  
libnss3-dev libnspr4-dev zlib1g-dev \  
libxml2-dev libidn11-dev libidn2-0-dev \  
libgtk2.0-dev libglib2.0-dev gconf2 && \  
apt-get clean  
  
USER buildbot  

