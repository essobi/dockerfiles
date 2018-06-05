FROM ubuntu:14.04  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
RUN apt-get update -y && apt-get install -y software-properties-common python-
software-properties build-essential libxml2-utils rtmpdump wget git zlib1g-dev  
RUN mkdir /var/src  
WORKDIR /var/src  
RUN wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz &&
tar zxvf yasm-1.2.0.tar.gz && cd yasm-1.2.0 && ./configure && make && make
install  
RUN wget
http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz &&
tar zxvf lame-3.99.5.tar.gz && cd lame-3.99.5 && ./configure && make && make
install  
RUN git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg && cd ffmpeg &&
./configure --enable-libmp3lame && make && make install  
RUN git clone git://github.com/matthiaskramm/swftools.git swftools && cd
swftools && ./configure && make && make install  
RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf && ldconfig  
ADD rec_radiko2.sh /usr/local/bin/rec_radiko2.sh  
RUN chmod +x /usr/local/bin/rec_radiko2.sh  
RUN mkdir /var/radiko  
WORKDIR /var/radiko  
ENTRYPOINT ["/usr/local/bin/rec_radiko2.sh"]  
  

