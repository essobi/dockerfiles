FROM trickkiste/decklink:latest  
MAINTAINER Markus Kienast <mark@trickkiste.at>  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /tmp  
WORKDIR /tmp  
# Download all dependencies and build OBE  
RUN apt-get update && \  
apt-get install -y git wget curl build-essential && \  
\  
wget \--quiet -O /tmp/yasm-1.2.0.tar.gz
http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz && \  
cd /tmp && tar -zxvf yasm-1.2.0.tar.gz && \  
cd yasm-1.2.0/ && ./configure \--prefix=/usr && make -j5 && make install && \  
\  
apt-get install -y libtwolame-dev autoconf libtool && \  
\  
cd /tmp && git clone https://github.com/ob-encoder/fdk-aac.git && \  
cd /tmp/fdk-aac && autoreconf -i && ./configure \--prefix=/usr \--enable-
shared && make -j5 && make install && \  
\  
cd /tmp && git clone https://github.com/ob-encoder/libav-obe.git && \  
cd /tmp/libav-obe && ./configure \--prefix=/usr \--enable-gpl \--enable-
nonfree \--enable-libfdk-aac \  
\--disable-swscale-alpha \--disable-avdevice && make -j5 && make install && \  
\  
cd /tmp && git clone https://github.com/ob-encoder/x264-obe.git && \  
cd /tmp/x264-obe && ./configure \--prefix=/usr \--disable-lavf \--disable-
swscale \--disable-opencl && \  
make -j5 && make install-lib-static && \  
\  
cd /tmp && git clone https://github.com/ob-encoder/libmpegts-obe.git && \  
cd /tmp/libmpegts-obe && ./configure \--prefix=/usr && make -j5 && make
install && \  
\  
apt-get install -y libzvbi0 libzvbi-dev libzvbi-common libreadline-dev && \  
\  
cd /tmp && git clone -b config-file https://github.com/gfto/obe-rt.git && \  
cd /tmp/obe-rt && export PKG_CONFIG_PATH=/usr/lib/pkgconfig && \  
./configure \--prefix=/usr && make -j5 && make install && \  
\  
apt-get install -y libtwolame0 && \  
\  
apt-get remove -y libreadline-dev libzvbi-dev libtwolame-dev \  
autoconf libtool git wget curl \  
manpages manpages-dev g++ g++-4.6 build-essential && \  
\  
apt-get autoclean -y && apt-get autoremove -y && apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -r /tmp/*  
  
COPY obe.conf /etc/obe.conf  
RUN useradd -m default  
  
WORKDIR /home/default  
  
USER default  
ENV HOME /home/default  
  
CMD ["/usr/bin/obecli","--config-file=/etc/obe.conf"]  

