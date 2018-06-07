FROM golang:1.8  
# Update  
RUN apt-get update -y  
  
ENV PACKAGES "g++-4.9 libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev"  
ENV CXX "g++-4.9"  
ENV CC "gcc-4.9"  
ENV ROCKSDB_RELEASE "v4.13.5"  
ENV BUILD_DIR "/tmp/rocks_build_dir"  
# RocksDB make method  
ENV ROCKSDB_MAKE_METHOD shared_lib  
  
# RocksDB release name  
ENV ROCKSDB_NAME "rocksdb_${ROCKSDB_RELEASE}"  
# Installing packages  
RUN apt-get install -y $PACKAGES  
  
# Clone & compile rocksdb  
RUN mkdir $BUILD_DIR && cd $BUILD_DIR \  
&& git clone https://github.com/facebook/rocksdb.git $ROCKSDB_NAME \  
&& cd $ROCKSDB_NAME && git checkout $ROCKSDB_RELEASE \  
&& make clean && make $ROCKSDB_MAKE_METHOD \  
&& cp --preserve=links ./librocksdb.* /usr/lib/ \  
&& cp -r ./include/rocksdb/ /usr/include/  
  
# Cleanup  
RUN rm -rf $BUILD_DIR \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc && rm -rf /usr/share/man \  
&& apt-get clean  

