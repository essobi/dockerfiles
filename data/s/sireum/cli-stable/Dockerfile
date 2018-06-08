FROM ubuntu:14.04  
MAINTAINER Robby <robby@santoslab.org>  
RUN apt-get update && \  
apt-get install -y wget lib32stdc++6 lib32z1 && \  
cd /usr/lib32 && \  
ln -sf libstdc++.so.6 libc++.so && \  
cd /opt && \  
wget -q https://bintray.com/artifact/download/sireum/cli/sireum-cli-stable-
linux64.tar.gz.part_00 && \  
wget -q https://bintray.com/artifact/download/sireum/cli/sireum-cli-stable-
linux64.tar.gz.part_01 && \  
wget -q https://bintray.com/artifact/download/sireum/cli/sireum-cli-stable-
linux64.tar.gz.part_02 && \  
cat *.part_* | tar xz && \  
rm *.part_*  
ENV PATH /opt/Sireum:$PATH  

