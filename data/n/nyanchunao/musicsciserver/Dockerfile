FROM ipython/scipyserver:latest  
MAINTAINER Nyan Chu<^o-o^>  
  
#install SPTK  
RUN apt-get install -y wget csh  
RUN wget http://downloads.sourceforge.net/sp-tk/SPTK-3.8.tar.gz -P /opt  
RUN tar zxvf /opt/SPTK-3.8.tar.gz -C /opt  
RUN cd /opt/SPTK-3.8 && ./configure && make && make install  
  
#install sox & lame  
RUN apt-get install -y sox lame  
  
#install ffmpeg  
RUN apt-get install -y build-essential automake autoconf zlib1g-dev libtool
libx264-dev yasm  
RUN wget http://ffmpeg.org/releases/ffmpeg-2.6.tar.gz -P /opt  
RUN tar zxvf /opt/ffmpeg-2.6.tar.gz -C /opt  
RUN cd /opt/ffmpeg-2.6 && /opt/ffmpeg-2.6/configure --enable-libx264 --enable-
gpl && make && make install  
  

