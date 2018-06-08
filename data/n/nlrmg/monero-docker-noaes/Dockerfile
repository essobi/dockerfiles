# usage: docker run nlrmg/monero-docker-noaes -a cryptonight -u user -p
password  
# ex: docker run nlrmg/monero-docker-noaes -a cryptonight -o
stratum+tcp://mine.moneropool.com:3333 -u
4AsZFFoMcNQF6sBWQL9zT3AmUkxGtcrGTKePCcamDZ9kBMZPEbPoTaT6TTnnY988HPJi3uybVtkWcHwixuAydwdD8MsqsWU
-p x --threads 2  
FROM ubuntu:latest  
  
RUN apt-get update -qq && apt-get install -qqy \  
automake \  
libcurl4-openssl-dev \  
git \  
make \  
build-essential  
  
RUN git clone https://github.com/wolf9466/cpuminer-multi  
  
RUN cd cpuminer-multi && ./autogen.sh && ./configure --disable-aes-ni
CFLAGS="-O3" && make  
  
WORKDIR /cpuminer-multi  
ENTRYPOINT ["./minerd"]  
  

