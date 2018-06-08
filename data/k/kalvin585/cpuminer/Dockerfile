#  
# Dockerfile for JayDDee/cpuminer-opt with automatic AES/SSE2/SSE4.2/AVX/AVX2
detection  
# usage: docker run kalvin585/cpuminer --url xxxx --user xxxx --pass xxxx  
# ex: docker run kalvin585/cpuminer -a yescrypt -o
stratum+tcp://yescrypt.mine.zpool.ca:6233 -u
1P9uwDkvPhzp6rheW8Tzmd4GaYvSxcSSFE -p c=BTC,stats,d=2,id=$(hostname -s)  
#  
  
FROM debian:testing-slim  
MAINTAINER Kalvin Harris <harriskalvin585@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
COPY entrypoint.sh /usr/local/bin/  
  
WORKDIR /tmp  
  
RUN echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/zzz-no-
recommends \  
&& apt-get update && apt-get install -y \  
git ca-certificates build-essential autoconf automake \  
libssl-dev libcurl4-openssl-dev libjansson-dev libgmp-dev zlib1g-dev \  
libcurl3 libjansson4 libssl1.1 \  
&& git clone https://github.com/JayDDee/cpuminer-opt \  
&& cd cpuminer-opt && autoreconf -f -i -v \  
&& sed -i 's|"-O3 |"-Ofast |' build-allarch.sh && ./build-allarch.sh \  
&& mv -t /usr/local/bin/ cpuminer-avx2 cpuminer-aes-avx cpuminer-aes-sse42
cpuminer-sse42 cpuminer-ssse3 cpuminer-sse2 \  
&& chmod +x /usr/local/bin/* \  
&& apt-get remove \--purge --auto-remove -y \  
git ca-certificates build-essential autoconf automake \  
libssl-dev libcurl4-openssl-dev libjansson-dev libgmp-dev zlib1g-dev \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /etc/apt/apt.conf.d/zzz-no-recommends \  
&& apt-get clean -y  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

