FROM linuxserver/plex:latest  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
git \  
libargtable2-dev \  
libsdl1.2-dev \  
autoconf \  
libtool \  
libavutil-dev \  
libavformat-dev \  
libavcodec-dev \  
ffmpeg \  
mkvtoolnix \  
&& \  
  
mkdir -p /plexbin && \  
git clone https://github.com/erikkaashoek/Comskip.git && \  
git clone https://github.com/ekim1337/PlexComskip.git && \  
cd /Comskip && ./autogen.sh && ./configure && make && make install && \  
cp comskip /plexbin && \  
cd /PlexComskip && cp comskip.ini PlexComskip.py /plexbin && cp
PlexComskip.conf.example /plexbin/PlexComskip.conf && \  
cp `which ffmpeg` /plexbin && \  
cp `which mkvpropedit` /plexbin  

