FROM nvidia/cuda:8.0-devel-ubuntu16.04  
# activate the required PPA  
RUN apt-get -qq update \  
&& apt-get -yqq --no-install-recommends install software-properties-common \  
&& add-apt-repository -y ppa:ethereum/ethereum  
  
# install the dev and the not dev packages so we can remove the dev packages
later to make  
# the image smaller  
RUN apt-get -qq update && \  
apt-get -yqq --no-install-recommends install \  
git cmake libcryptopp-dev libleveldb-dev libjsoncpp-dev libjsonrpccpp-dev \  
libboost-all-dev libgmp-dev libreadline-dev libcurl4-gnutls-dev \  
ocl-icd-libopencl1 opencl-headers mesa-common-dev libmicrohttpd-dev \  
build-essential  
  
# set up a user to compile everything  
RUN groupadd -r miner --gid=1001 \  
&& useradd -r -g miner --uid=1001 miner  
  
# create a folder to compile  
RUN mkdir /minerbuild \  
&& chown miner.miner /minerbuild  
  
# get the miner source code from git as the user  
USER miner  
RUN cd /minerbuild && \  
git clone https://github.com/Genoil/cpp-ethereum/  
  
# now build the code  
RUN cd /minerbuild/cpp-ethereum && \  
mkdir build && \  
cd build && \  
cmake -DBUNDLE=cudaminer .. && \  
make  
  
# Move the built miner to /app  
USER root  
RUN mkdir /app && \  
mkdir /app/lib && \  
chown -R miner.miner /app  
USER miner  
CMD ["/bin/bash"]  
RUN mv /minerbuild/cpp-ethereum/build/ethminer/ethminer /app && \  
mv /minerbuild/cpp-ethereum/build/**/*.so /app/lib  
  
# Do some cleanup  
USER root  
RUN rm -rf /minerbuild  
# Add the miner libraries to the LD library path  
RUN echo "/app/lib" > /etc/ld.so.conf.d/app.conf && \  
ldconfig  
  
USER miner  
ENTRYPOINT ["/app/ethminer"]  
  

