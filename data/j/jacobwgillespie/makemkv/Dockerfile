FROM jacobwgillespie/gui  
  
RUN \  
apt-get update -qq && \  
# Install dependencies  
apt-get install -qy \  
build-essential \  
less \  
libavcodec-dev \  
libc6-dev \  
libexpat1-dev \  
libgl1-mesa-dev \  
libqt4-dev \  
libssl-dev \  
pkg-config \  
wget && \  
# Fetch sources  
mkdir -p /tmp/sources && \  
wget -O /tmp/sources/makemkv-bin-1.10.4.tar.gz
http://www.makemkv.com/download/makemkv-bin-1.10.4.tar.gz && \  
wget -O /tmp/sources/makemkv-oss-1.10.4.tar.gz
http://www.makemkv.com/download/makemkv-oss-1.10.4.tar.gz && \  
wget -O /tmp/sources/ffmpeg-2.8.tar.bz2
https://ffmpeg.org/releases/ffmpeg-2.8.tar.bz2 && \  
cd /tmp/sources/ && \  
tar xvzf /tmp/sources/makemkv-bin-1.10.4.tar.gz && \  
tar xvzf /tmp/sources/makemkv-oss-1.10.4.tar.gz && \  
tar xvjf /tmp/sources/ffmpeg-2.8.tar.bz2 && \  
# Install ffmpeg  
cd /tmp/sources/ffmpeg-2.8 && \  
./configure --prefix=/tmp/ffmpeg --enable-static --disable-shared --enable-pic
--disable-yasm && \  
make install -j4 && \  
# Install makemkv-oss  
cd /tmp/sources/makemkv-oss-1.10.4 && \  
PKG_CONFIG_PATH=/tmp/ffmpeg/lib/pkgconfig ./configure && \  
make && \  
make install && \  
# Install makemkv-bin  
cd /tmp/sources/makemkv-bin-1.10.4 && \  
/bin/bash -c "/bin/echo -e 'yes' | make install" && \  
# Cleanup  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/*  
  
ADD /files/ /  
  
ENV APP_NAME=MakeMKV  
  
VOLUME /config  

