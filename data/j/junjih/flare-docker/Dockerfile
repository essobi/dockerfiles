FROM ubuntu:trusty  
MAINTAINER Junji Hashimoto "junji.hashimoto@gree.net"  
  
RUN sed -i s/archive/jp.archive/g /etc/apt/sources.list  
RUN apt-get update && \  
apt-get -y --force-yes install \  
autoconf \  
automake \  
libtool \  
make \  
gcc \  
g++ \  
libboost-all-dev \  
zlib1g-dev \  
libncursesw5 \  
git \  
libhashkit-dev \  
libtokyocabinet-dev \  
libkyotocabinet-dev \  
uuid-dev \  
libsqlite3-dev \  
libncurses5-dev \  
libcurl4-openssl-dev \  
devscripts \  
git-buildpackage \  
\--no-install-recommends && \  
apt-get clean && \  
git config --global http.sslVerify false && \  
cd /tmp && git clone https://github.com/gree/flare.git && \  
cd /tmp/flare && \  
./autogen.sh && ./configure && make install && \  
cd /tmp && rm -rf flare && \  
apt-get -y --force-yes purge \  
autoconf \  
automake \  
libtool \  
make \  
gcc \  
g++ \  
libboost-all-dev \  
zlib1g-dev \  
git \  
libhashkit-dev \  
libtokyocabinet-dev \  
libkyotocabinet-dev \  
uuid-dev \  
libsqlite3-dev \  
libncurses5-dev \  
libcurl4-openssl-dev \  
devscripts \  
git-buildpackage && \  
apt-get -y --force-yes autoremove && \  
apt-get -y --force-yes install \  
libkyotocabinet16 \  
libtokyocabinet9 \  
libhashkit2 \  
libboost-serialization1.54.0 \  
libboost-program-options1.54.0 \  
libboost-regex1.54.0 && \  
apt-get clean  
ADD flarei.conf /etc/flarei.conf  
ADD flared.conf /etc/flared.conf  
ADD run /usr/local/bin/run  
ENTRYPOINT "run"  

