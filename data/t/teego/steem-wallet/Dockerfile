# -*- coding: utf-8 -*-  
FROM teego/steem-devel:0.3-Ubuntu-xenial  
  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV BUILDBASE /r  
ENV BUILDROOT $BUILDBASE/build  
ENV FILESROOT $BUILDBASE/files  
  
RUN mkdir -p $BUILDROOT $FILESROOT  
  
ENV STEEM_VERSION 0.14.3  
RUN cd $BUILDROOT && \  
( \  
git clone https://github.com/TigerND/steem.git steem &&\  
cd steem ;\  
( \  
git submodule update --init --recursive &&\  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
CMakeLists.txt &&\  
make install \  
) \  
) &&\  
( \  
rm -Rf $BUILDROOT/steem \  
)  
  
RUN cd $BUILDROOT && \  
( \  
git clone https://github.com/TigerND/steem.git steem &&\  
cd steem ;\  
( \  
git submodule update --init --recursive &&\  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DLOW_MEMORY_NODE=ON \  
-DENABLE_CONTENT_PATCHING=OFF \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
CMakeLists.txt &&\  
make steemd &&\  
cp programs/steemd/steemd /usr/local/bin/steemd_lowmem \  
) \  
) &&\  
( \  
rm -Rf $BUILDROOT/steem \  
)  
  
RUN mkdir -p /witness_node_data_dir &&\  
touch /witness_node_data_dir/.default_dir  
  
ADD config.ini $FILESROOT/config.ini.sample  
  
ENV STEEMD_EXEC="/usr/local/bin/steemd"  
ENV STEEMD_ARGS="--p2p-endpoint=0.0.0.0:2001 --rpc-endpoint=0.0.0.0:8090
--replay-blockchain"  
ADD run-steemd.sh /usr/local/bin  
  
EXPOSE 2001 8090  
VOLUME ["/witness_node_data_dir"]  
  
CMD ["/usr/local/bin/run-steemd.sh"]  

