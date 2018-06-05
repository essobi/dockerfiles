FROM ubuntu:zesty  
  
ENV MAJOR_VERSION 2.78  
ENV BLENDER_VERSION 2.78c  
ENV BLENDER_URL
http://download.blender.org/release/Blender$MAJOR_VERSION/blender-$BLENDER_VERSION-
linux-glibc219-x86_64.tar.bz2  
  
LABEL authors="Monta <84monta@gmail.com>"  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
bzip2 \  
libfreetype6 \  
libgl1-mesa-dev \  
libglu1-mesa \  
libxi6 \  
libxrender1 && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/local/blender && \  
curl -SL "$BLENDER_URL" -o blender.tar.bz2 && \  
tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 && \  
rm blender.tar.bz2 && \  
curl -SL "https://github.com/84monta/blendenv/raw/master/master.blend" -o
/usr/local/blender/master.blend  
  
ENTRYPOINT ["/usr/local/blender/blender", "-b
/usr/local/blender/master.blend", "--addons netrender", "-a -noaudio",
"-nojoystick"]  

