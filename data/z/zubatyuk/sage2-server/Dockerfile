FROM ubuntu:trusty  
MAINTAINER Roman Zubatyuk <zubatyuk@gmail.com>  
  
RUN mkdir /root/BUILD  
COPY build-ffmpeg.sh build-imagemagic.sh /root/BUILD/  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
software-properties-common curl \  
&& apt-add-repository -y ppa:mc3man/trusty-media  
  
RUN curl https://deb.nodesource.com/setup_0.12 | bash -  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
nodejs build-essential libx264-dev yasm libnss3-tools git libimage-exiftool-
perl \  
wget python libwebp-dev libvorbis-dev libvpx-dev libnss3-tools libjpeg-dev \  
libpng-dev libtiff5-dev ghostscript libgs-dev \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN cd /root/BUILD \  
&& bash build-ffmpeg.sh \  
&& bash build-imagemagic.sh \  
&& ldconfig  
  
RUN cd / \  
&& git clone https://bitbucket.org/sage2/sage2.git \  
&& cd sage2/keys \  
&& ./GO-linux \  
&& cd .. \  
&& npm run in  
  
EXPOSE 9090 9292  
WORKDIR /sage2  
CMD ["node", "server.js"]  

