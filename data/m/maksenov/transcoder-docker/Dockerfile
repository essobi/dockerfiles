FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y software-properties-common python-software-properties
netcat nano && \  
add-apt-repository -y ppa:jonathonf/ffmpeg-3 && \  
apt-get update -y && \  
apt-get install -y ffmpeg libav-tools x264 x265 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
EXPOSE 9192  
COPY ffmpeg-server /usr/bin  
  
RUN chmod +x /usr/bin/ffmpeg-server  
  
#CMD [ /usr/bin/ffmpeg-server ]  

