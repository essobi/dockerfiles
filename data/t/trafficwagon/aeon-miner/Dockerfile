FROM ubuntu:18.04  
ENV ALGO="cryptonight-lite" URL="chicago01.aeon.hashvault.pro:5555"
USER="WmsXY45ouAQ17Kw5defE1GeDtQctgm151QNUgYYzWbMZSK7ZC6xcFz4WBPfVvx7ZaaX7wmPqbA1VWhtU82FzffGb1xtZRK6QS"
NAME="miner1" AUTONAME="false" THREADS="1" RECOMMENDTHREADS="true" AV="0"
KEEPALIVE="true" RETRIES="5" RETRYPAUSE="5" CPUPRIORITY="5"
NOHUGEPAGES="false" NOCOLOR="false" MAXCPUUSAGE="100"  
RUN apt-get update && \  
apt-get install -y \  
bc \  
build-essential \  
cmake \  
git \  
gpp \  
libuv1-dev && \  
git clone https://github.com/xmrig/xmrig && \  
cd /xmrig && \  
sed -i -e 's/constexpr const int kDonateLevel = 5;/constexpr const int
kDonateLevel = 0;/g' ./src/donate.h && \  
mkdir build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF . && \  
make  
  
COPY start.sh /xmrig/  
RUN chmod +x /xmrig/start.sh  
WORKDIR /xmrig  
  
ENTRYPOINT ["./start.sh"]  

