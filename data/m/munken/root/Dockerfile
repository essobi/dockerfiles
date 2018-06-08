FROM ubuntu:trusty  
  
ARG APT_PROXY_PORT=  
COPY detect-apt-proxy.sh /root  
RUN /root/detect-apt-proxy.sh ${APT_PROXY_PORT}  
  
RUN apt-get update && apt-get install -y \  
git cmake libunittest++-dev libcurl4-openssl-dev ca-certificates make g++ gcc
\  
binutils libx11-dev libxpm-dev libxft-dev \  
libxext-dev libpng12-dev libjpeg-turbo8-dev \  
python gfortran libssl-dev wget libgsl0-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ROOT_TAR="root_v6.05.02.Linux-ubuntu14-x86_64-gcc4.8.tar.gz"  
ENV ROOT_DL="https://root.cern.ch/download/$ROOT_TAR"  
ENV ROOTSYS="/cern/root/"  
ENV PATH="$ROOTSYS/bin:$PATH"  
ENV LD_LIBRARY_PATH="$ROOTSYS/lib:$LD_LIBRARY_PATH"  
RUN mkdir /cern && cd /cern \  
&& wget $ROOT_DL \  
&& tar xzfv $ROOT_TAR \  
&& rm -rf $ROOT_TAR  

