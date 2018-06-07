FROM debian:jessie  
LABEL maintainer "mikael.brorsson@gmail.com"  
  
ENV BUILDROOT_VERSION buildroot-2017.02  
  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
wget \  
cpio \  
python \  
unzip \  
rsync \  
bc \  
subversion \  
squashfs-tools \  
libncurses5-dev \  
git && \  
\  
\  
mkdir -p /src && \  
wget -q https://buildroot.uclibc.org/downloads/$BUILDROOT_VERSION.tar.gz -O -
| tar xzf - -C /src && \  
\  
\  
echo "====> clean up..." && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p /src/$BUILDROOT_VERSION/output && \  
mkdir -p /images && \  
ln -sf /images /src/$BUILDROOT_VERSION/output/images  
  
VOLUME ["/images"]  
  
WORKDIR /src/$BUILDROOT_VERSION  

