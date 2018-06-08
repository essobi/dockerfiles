FROM ubuntu:trusty  
MAINTAINER Keichi Takahashi <keichi.t@me.com>  
  
RUN \  
apt-get update -y && \  
apt-get install -y build-essential libx264-dev yasm libnss3-tools git \  
libimage-exiftool-perl wget python pkg-config libwebp-dev devscripts && \  
cd /tmp && \  
wget -O - http://nodejs.org/dist/node-latest.tar.gz | tar xzvf - && \  
cd node-v* && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
wget -O - https://github.com/FFmpeg/FFmpeg/archive/n2.2.15.tar.gz | tar xzvf -
&& \  
cd FFmpeg-n2.2.15 && \  
./configure --enable-gpl --enable-libx264 --enable-shared && \  
make && \  
make install && \  
ldconfig && \  
cd /tmp && \  
mkdir imagemagick && \  
cd imagemagick && \  
apt-get build-dep -y imagemagick && \  
apt-get source -y imagemagick && \  
cd imagemagick-* && \  
debuild -uc -us && \  
dpkg -i ../*magick*.deb ; \  
ln -s /usr/bin/convert.im6 /usr/bin/convert && \  
cd / && \  
git clone https://bitbucket.org/sage2/sage2.git && \  
cd sage2/keys && \  
./GO-linux && \  
cd .. && \  
npm install && \  
apt-get clean -y && \  
rm -r /tmp/*  
  
EXPOSE 9090 9292  
WORKDIR /sage2  
CMD ["node", "server.js"]  
  

