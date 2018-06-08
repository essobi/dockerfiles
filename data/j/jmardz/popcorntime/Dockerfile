FROM ubuntu:16.04  
MAINTAINER jmardz  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libglib2.0-0 \  
libnss3 \  
libcups2 \  
libx11-6 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxi6 \  
libxtst6 \  
libexpat-gst \  
libfontconfig1 \  
libgconf-2-4 \  
libpangocairo-1.0-0 \  
libxss1 \  
libxrandr2 \  
libatk-adaptor \  
libasound2 \  
pulseaudio \  
libgl1-mesa-glx \  
wget \  
xz-utils && \  
cd /opt && \  
wget https://get.popcorntime.sh/repo/build/Popcorn-Time-0.3.10-Linux-64.tar.xz
-O popcorntime-tar --no-check-certificate && \  
mkdir popcorntime && \  
tar -xf popcorntime-tar -C popcorntime && \  
rm popcorntime-tar  
  
ENV PULSE_SERVER /run/pulse/native  
  
ENTRYPOINT ["/opt/popcorntime/Popcorn-Time"]  
  
  

