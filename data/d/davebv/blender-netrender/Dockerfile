FROM ubuntu:xenial  
LABEL maintainer="davebv"  
  
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
  
RUN mkdir /usr/local/blender  
ADD startup.py /root/  
# Needed for startup.py  
RUN mkdir /root/blender-tmp  
  
# curl -SL https://www.blender.org/download/Blender2.79/blender-2.79b-linux-
glibc219-x86_64.tar.bz2/ | grep bz2 | sed -e 's/.*href="\\(.*\\)">.*/\1/' >>
download_tmp.txt  
ARG BLENDER_BZ2_URL=https://ftp.halifax.rwth-
aachen.de/blender/release/Blender2.79/blender-2.79b-linux-
glibc219-x86_64.tar.bz2  
RUN curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 && \  
tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 && \  
rm blender.tar.bz2  
  
#RUN apt-get update && apt-get dist-upgrade -y  
#RUN apt-get install -y software-properties-common  
#  
#RUN add-apt-repository ppa:thomas-schiex/blender  
#RUN apt-get update && apt-get install -y
blender=2.79.b~1521727842-0thomas~bionic0  
CMD ["/usr/local/blender/blender", "-b", "-P", "/root/startup.py", "-noaudio",
"-a", "-nojoystick", "--addons", "netrender"]  

