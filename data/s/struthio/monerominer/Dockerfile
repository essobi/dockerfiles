FROM ubuntu:17.04  
WORKDIR /tmp/monero  
  
RUN apt-get update && \  
apt-get -y install git libcurl4-openssl-dev build-essential libjansson-dev
autotools-dev automake && \  
git clone https://github.com/wolf9466/cpuminer-multi . && \  
./autogen.sh && \  
CFLAGS="-march=native" ./configure && \  
make && \  
make install && \  
rm -r /tmp/monero && \  
apt-get -y purge git libcurl4-openssl-dev build-essential libjansson-dev
autotools-dev automake  
  
WORKDIR /tmp  
ENTRYPOINT ["/usr/local/bin/minerd"]  

