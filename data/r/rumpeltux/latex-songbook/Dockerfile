FROM ubuntu:xenial  
MAINTAINER Hagen Fritsch <rumpeltux-songbookdocker@irgendwo.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q && \  
apt-get install -qy texlive-full python-pygments gnuplot wget make \  
software-properties-common python-software-properties  
  
# Install mscorefonts for "Courier New"  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu wily
multiverse" && \  
apt-get update -q && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
apt-get -qy install ttf-mscorefonts-installer  
  
# Install MuseJazz font  
RUN mkdir -p /usr/share/fonts/truetype/music && \  
wget
'https://github.com/musescore/MuseScore/blob/master/fonts/MuseJazz.ttf?raw=true'
\  
-O /usr/share/fonts/truetype/music/MuseJazz.ttf && \  
fc-cache -f -v  
  
# Install more packages that are needed now that the songbook evolved.  
RUN apt-get install -qy --no-install-recommends git python-pyparsing lilypond  
  
WORKDIR /data  
VOLUME ["/data"]  

