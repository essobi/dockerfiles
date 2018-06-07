FROM ubuntu:14.04  
MAINTAINER ed@table.co  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common python build-essential  
RUN apt-get install -y curl ghostscript git graphicsmagick imagemagick libav-
tools poppler-utils wget  
  
ENV FFMPEG_VERSION=3.0.1 \  
X264_VERSION=snapshot-20160416-2245-stable  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y bzip2 libgnutlsxx27
libogg0 libjpeg8 libpng12-0 \  
libvpx1 libtheora0 libxvidcore4 libmpeg2-4 \  
libvorbis0a libfaad2 libmp3lame0 libmpg123-0 libmad0 libopus0 libvo-aacenc0 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY install.sh /var/cache/ffmpeg/install.sh  
RUN bash /var/cache/ffmpeg/install.sh  
  
# node  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo bash -  
RUN apt-get install -y nodejs  
  

