FROM krot/srk-cuda-base  
MAINTAINER Oleg Shyshkov <shyshkov.oleg@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cmake \  
git \  
libboost-filesystem-dev \  
libboost-system-dev \  
libboost-random-dev \  
libboost-thread-dev \  
libboost-program-options-dev \  
libnetcdf-dev  
  
RUN git clone https://github.com/olage/currennt.git /root/currennt && \  
mkdir /root/currennt/build && \  
cd /root/currennt/build && \  
cmake .. && \  
make && \  
cp currennt /usr/bin/ && \  
cd /root && \  
rm -r currennt  

