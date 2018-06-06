# usage: docker run creepycat/monero-miner -a -o POOLINFO cryptonight -u user
-p password  
# ex: docker run kannix/monero-miner -a cryptonight -o
stratum+tcp://mine.moneropool.com:3333 -u
4AsZFFoMcNQF6sBWQL9zT3AmUkxGtcrGTKePCcamDZ9kBMZPEbPoTaT6TTnnY988HPJi3uybVtkWcHwixuAydwdD8MsqsWU
-p x --threads 2  
FROM debian:9  
RUN apt-get update -qq && apt-get install -qqy \  
automake libcurl4-openssl-dev \  
git make build-essential  
  
RUN apt-get clean  
  
RUN git clone \--recursive https://github.com/OhGodAPet/cpuminer-multi.git  
  
RUN cd cpuminer-multi && ./autogen.sh && ./configure CFLAGS="-O3" && make  
  
WORKDIR /cpuminer-multi  
ENTRYPOINT ["./minerd"]  

