FROM ubuntu:14.04  
MAINTAINER martin@gabelmann.biz  
  
ENV ROOT_TAR="root_v6.08.04.Linux-ubuntu14-x86_64-gcc4.8.tar.gz"  
ENV ROOT_DL="https://root.cern.ch/download/$ROOT_TAR"  
  
ENV ROOTSYS="/cern/root/"  
ENV PATH="$ROOTSYS/bin:$PATH"  
ENV LD_LIBRARY_PATH="$ROOTSYS/lib:$LD_LIBRARY_PATH"  
RUN apt-get update && apt-get upgrade -y &&\  
apt-get install --no-install-recommends -y git dpkg-dev make g++ gcc \  
binutils libx11-dev libxpm-dev libxft-dev \  
libxext-dev libpng12-dev libjpeg-turbo8-dev \  
python gfortran libssl-dev wget &&\  
mkdir /cern && cd /cern &&\  
wget -nv --no-check-certificate $ROOT_DL &&\  
apt-get purge -y wget && apt-get autoremove -y && apt-get clean &&\  
tar xzf $ROOT_TAR &&\  
rm -rf $ROOT_TAR  
ADD run-root /usr/local/sbin/run-root  
  
WORKDIR /tmp/  
  
ENTRYPOINT ["run-root"]  

