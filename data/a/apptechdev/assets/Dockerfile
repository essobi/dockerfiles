FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -yq build-essential software-properties-common python-
software-properties curl && \  
add-apt-repository ppa:jonathonf/ffmpeg-3 && \  
apt-get update && \  
apt-get install -yq graphicsmagick imagemagick ffmpeg libav-tools x264 x265  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -yq nodejs  
  
WORKDIR /usr/src  
  
EXPOSE 8000  

