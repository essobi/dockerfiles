FROM debian:wheezy  
  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y build-essential \  
automake \  
libtool \  
devscripts \  
libncurses5-dev \  
exuberant-ctags \  
git \  
wget \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/taotao/global-deb.git /root/global-deb && \  
cd /root/global-deb && \  
wget ftp://ftp.gnu.org/pub/gnu/global/global-6.5.tar.gz && \  
make  

