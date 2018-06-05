  
FROM teego/steem-base:0.2  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN echo "Boost library" &&\  
( \  
apt-get install -qy --no-install-recommends \  
libboost-all-dev \  
) && \  
apt-get clean -qy  
  
RUN mkdir -p /root/src && \  
( \  
git clone https://github.com/TigerND/steem.git steem &&\  
cd steem ;\  
( \  
git checkout replay-blockchain-and-exit &&\  
git submodule update --init --recursive &&\  
cmake \  
-DENABLE_CONTENT_PATCHING=OFF \  
-DLOW_MEMORY_NODE=OFF \  
CMakeLists.txt &&\  
make install \  
) \  
) &&\  
( \  
cd /root/src ;\  
rm -Rf steem \  
)  
  
RUN mkdir -p /steem  
  
ADD config.ini /steem  
  
RUN /usr/local/bin/steemd --data-dir /steem --resync-blockchain --startup-only
|| /bin/true  
  
CMD ["/bin/bash"]  

