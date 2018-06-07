# DECENT Dockerfile  
# Based on Someguy123's Peerplays-in-a-box  
# Modified for DECENT by @yangwao  
# cd ~/dkr && docker build -t decent .  
# docker run -p 0.0.0.0:9777:9777 -v $PWD/data:/decent -d -t decent  
FROM ubuntu:xenial  
RUN apt-get update && \  
apt-get install -y gcc-4.9 g++-4.9 cmake make libbz2-dev libdb++-dev libdb-dev
&& \  
apt-get install -y libssl-dev openssl libreadline-dev autoconf libtool git &&
\  
apt-get install -y autotools-dev build-essential g++ libbz2-dev libicu-dev
python-dev wget doxygen python3 python3-dev libboost-all-dev curl && \  
apt-get clean -qy  
  
RUN apt-get install build-essential autotools-dev automake autoconf libtool
make cmake checkinstall realpath gcc g++ clang flex bison doxygen gettext git
qt5-default libqt5svg5-dev libreadline-dev libcrypto++-dev libgmp-dev libdb-
dev libdb++-dev libssl-dev libncurses5-dev libboost-all-dev libcurl4-openssl-
dev python-dev libicu-dev libbz2-dev -qy  
  
# install boost  
RUN wget
https://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.gz
&& \  
tar xvf boost_1_60_0.tar.gz && \  
mkdir boost-1.60.0_prefix && \  
cd boost_1_60_0 && \  
export BOOST_ROOT=$(realpath ../boost-1.60.0_prefix) && \  
./bootstrap.sh --prefix=$BOOST_ROOT && \  
./b2 install  
  
ENV BOOST_ROOT /boost-1.60.0_prefix  
  
  
# ARG decentd_version=0.1.8  
run cd / && \  
git clone https://github.com/decentfoundation/decent-network decent-src && \  
cd decent-src && \  
git checkout stage && \  
git submodule update --init --recursive  
  
RUN cd / && \  
mkdir decent-bin && \  
cd decent-bin && \  
cmake -G "Unix Makefiles" -D CMAKE_BUILD_TYPE=Release /decent-src && \  
cmake --build . --target all -- -j -l 3.0 && \  
cmake --build . --target install  
  
# P2P (seed) port  
# EXPOSE 2001  
# API Port  
# EXPOSE 8090  
RUN cp /decent-bin/artifacts/prefix/bin/* /decent-bin  
VOLUME /root/.decent  
WORKDIR /decent-bin  
ENTRYPOINT ["sh", "-c", "/decent-bin/decentd"]  

