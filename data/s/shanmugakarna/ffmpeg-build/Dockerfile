FROM ubuntu:16.04  
MAINTAINER Shan<shanmuga_karna@yahoo.com>  
  
ENV FFMPEG_VERSION 3.1.1  
  
RUN echo 'deb http://www.deb-multimedia.org sid main' >> /etc/apt/sources.list
&& \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5C808C2B65558117 && \  
apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y wget bzip2 build-essential yasm libass-dev libfaac-dev
libfaac-dev libfdk-aac-dev \  
libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libopus-dev
libpulse-dev libsoxr-dev \  
libspeex-dev libvidstab-dev libvorbis-dev libvpx-dev libx264-dev libx265-dev
libxvidcore-dev libssl-dev  
  
WORKDIR /opt  
ADD build.sh /  
  
ENTRYPOINT ["./build.sh"]  
  
CMD ["3.1.1"]  

