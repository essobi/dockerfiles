# Ikaros on Linux  
#FROM ubuntu:14.04  
FROM debian:wheezy  
  
MAINTAINER Pooya Parsa <pooya@pi0.ir>  
  
# Add Ubuntu Repository  
RUN \  
echo "deb http://ch.archive.ubuntu.com/ubuntu/ trusty main" >>
/etc/apt/sources.list && \  
echo 'APT::Get::AllowUnauthenticated "true";' >
/etc/apt/apt.conf.d/99AllowUnauthenticated  
  
# Install dependencies  
RUN \  
apt-get update && apt-get install -y --force-yes \  
curl \  
cmake \  
g++ \  
libjpeg-turbo8-dev \  
libgsl0-dev \  
libpng-dev \  
libblas-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev  
  
  
# Download the Ikaros source  
RUN \  
curl -SL http://github.com/ikaros-project/ikaros/archive/master.tar.gz | \  
tar -xzf - && \  
mv ikaros-master ikaros  
  
  
# Build Ikaros  
RUN \  
cd ikaros/Build && \  
cmake .. && \  
make && \  
ln -fvs /ikaros/Bin/ikaros /usr/local/bin && \  
ln -fvs /ikaros/Examples /Examples  
  
# SlimDown Container  
RUN \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/*  
  
# Entry point  
ENTRYPOINT [ "/ikaros/Bin/ikaros" ]  

