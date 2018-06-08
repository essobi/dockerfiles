FROM debian:buster-20180312  
  
RUN sed -i 's/main/main non-free/' /etc/apt/sources.list  
  
RUN apt-get update -y -qq && \  
apt-get install -y -qq \  
libboost-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libboost-timer-dev \  
libfdk-aac-dev \  
libjsoncpp-dev \  
libopencv-imgproc-dev \  
libopencv-highgui-dev \  
libpng-dev \  
librsvg2-dev \  
libxml2-dev \  
libxslt1-dev \  
libtiff5-dev \  
libjpeg-dev \  
zlib1g-dev \  
libfreetype6-dev \  
liblcms2-dev \  
libffi-dev \  
libssl-dev \  
libx264-dev \  
libglew-dev \  
liblz4-dev \  
libopenexr-dev \  
libucimf-dev \  
libcurl4-openssl-dev \  
libavutil-dev \  
libswscale-dev \  
libavresample-dev \  
libavformat-dev \  
libavcodec-dev \  
libthai-dev \  
wget jq awscli  
  
RUN mkdir /app  
WORKDIR /app  

