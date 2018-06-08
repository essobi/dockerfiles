# git clone https://github.com/goldendict/goldendict $HOME/src/goldendict  
# docker run --rm -v $HOME/src/goldendict:/home/build/src liyin/goldendict  
FROM ubuntu:16.04  
MAINTAINER Li Yin <liyin@live.com>  
  
RUN apt-get update && apt-get install -y git pkg-config build-essential
qt4-qmake \  
libvorbis-dev zlib1g-dev libhunspell-dev x11proto-record-dev \  
libqt4-dev libqtwebkit-dev libxtst-dev liblzo2-dev libbz2-dev \  
libao-dev libavutil-dev libavformat-dev libtiff5-dev libeb16-dev \  
libopencc-dev && \  
apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
adduser --disabled-password --gecos "" build  
  
USER build  
WORKDIR /home/build/src  
CMD qmake-qt4 && make  

