FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
libssl-dev \  
libhwloc-dev \  
cmake \  
libmicrohttpd-dev \  
git \  
ca-certificates && \  
# python3 && \  
rm -rf /var/lib/apt/lists/* && \  
git clone https://github.com/fireice-uk/xmr-stak.git && \  
mkdir xmr-stak/build && \  
cd xmr-stak/build && \  
cmake -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF .. && \  
make install && \  
apt-get -y purge \  
build-essential \  
cmake \  
git && \  
apt-get autoremove -y --purge && \  
apt-get clean -y && \  
cp /xmr-stak/build/bin/xmr-stak /xmrstak  
  
CMD ["/xmrstak"]

