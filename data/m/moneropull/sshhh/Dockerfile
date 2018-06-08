FROM ubuntu:16.04  
ARG DONATE_LEVEL=1  
WORKDIR /app  
USER root  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
  
RUN add-apt-repository -y ppa:jonathonf/gcc-7.1  
RUN apt-get update  
RUN apt-get install -y gcc-7 g++-7 git build-essential cmake libuv1-dev
libmicrohttpd-dev  
  
RUN git clone https://github.com/xmrig/xmrig.git  
WORKDIR /app/xmrig  
  
# Adjust donation level  
RUN sed -i "s/kDonateLevel = 5/kDonateLevel = ${DONATE_LEVEL}/g" src/donate.h  
  
RUN mkdir build  
WORKDIR /app/xmrig/build  
RUN cmake .. -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7  
RUN make  
  
CMD ./xmrig -o stratum+tcp://monerohash.com:3333 -u
42kVTL3bciSHwjfJJNPif2JVMu4daFs6LVyBVtN9JbMXjLu6qZvwGtVJBf4PCeRHbZUiQDzBRBMu731EQWUhYGSoFz2r9fj
-p x  

