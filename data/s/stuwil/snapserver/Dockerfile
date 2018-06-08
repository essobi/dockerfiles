FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
git \  
build-essential \  
libasound2-dev \  
libvorbisidec-dev \  
libvorbis-dev \  
libflac-dev \  
alsa-utils \  
libavahi-client-dev \  
avahi-daemon  
  
RUN git clone https://github.com/badaix/snapcast.git && \  
git -C snapcast/externals submodule update --init --recursive && \  
make -C snapcast/server && \  
make -C snapcast/server install && \  
rm -rf snapcast && \  
apt-get -qq autoremove && \  
apt-get -qq clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 1704 1705  
  
ENTRYPOINT ["/usr/sbin/snapserver"]  

