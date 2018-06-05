FROM nvidia/cuda:7.5-runtime  
MAINTAINER Yu You <yu.you@nokia.com>  
ENV BLENDER_MAJOR 2.76  
ENV BLENDER_VERSION 2.76b  
ENV BLENDER_BZ2_URL
http://mirror.cs.umn.edu/blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-
linux-glibc211-x86_64.tar.bz2  
  
RUN apt-get update && \  
apt-get install -y \  
curl wget nano \  
bzip2 libfreetype6 libgl1-mesa-dev \  
libglu1-mesa \  
libxi6 && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/local/blender && \  
curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 && \  
tar -jxvf blender.tar.bz2 -C /usr/local/blender \--strip-components=1 && \  
rm blender.tar.bz2  
  
RUN ln -s /usr/local/blender/blender /usr/bin/blender  
  
VOLUME /data  
  
RUN cd /tmp && curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  

