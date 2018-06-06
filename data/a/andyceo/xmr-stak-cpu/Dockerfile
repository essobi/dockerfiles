FROM debian:stretch-slim as builder  
WORKDIR /root  
RUN apt-get update -qq && apt-get install -qqy git libmicrohttpd-dev libssl-
dev cmake build-essential libhwloc-dev && \  
git clone https://github.com/fireice-uk/xmr-stak.git && \  
sed -i 's/constexpr double fDevDonationLevel.*/constexpr double
fDevDonationLevel = 0.0;/' xmr-stak/xmrstak/donate-level.hpp && \  
mkdir xmr-stak/build && \  
cd xmr-stak/build && \  
cmake -DCMAKE_LINK_STATIC=ON \  
-DXMR-STAK_COMPILE=generic \  
-DCMAKE_BUILD_TYPE=Release \  
-DMICROHTTPD_ENABLE=ON \  
-DOpenSSL_ENABLE=ON \  
-DXMR-STAK_CURRENCY=monero \  
-DHWLOC_ENABLE=ON \  
-DCPU_ENABLE=ON \  
-DOpenCL_ENABLE=OFF \  
-DCUDA_ENABLE=OFF \  
.. && \  
make install  
  
FROM debian:stretch-slim  
MAINTAINER Andrey Andreev <andyceo@yandex.ru> (@andyceo)  
LABEL RUN /usr/bin/docker run -d --restart=always -v ~/xmr-stak-cpu-
config.txt:/app/config.txt andyceo/xmr-stak-cpu --config /app/config.txt  
LABEL GET_CONFIG /usr/bin/docker run --rm -ti andyceo/xmr-stak-cpu  
RUN apt-get update -qq && apt-get install -qqy --no-install-recommends
libmicrohttpd12 libssl1.1 libhwloc5 && \  
mkdir /app && \  
apt-get clean && apt-get autoremove && rm -r /var/lib/apt/lists/* && rm -rf
/tmp/* /var/tmp/*  
WORKDIR /app  
COPY \--from=builder /root/xmr-stak/build/bin/xmr-stak /app/xmr-stak-cpu  
ENTRYPOINT ["/app/xmr-stak-cpu"]  
CMD []  

