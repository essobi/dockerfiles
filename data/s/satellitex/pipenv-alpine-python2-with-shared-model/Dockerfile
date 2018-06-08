FROM ktr0731/pipenv-alpine-python2-with-nodejs  
  
USER root  
RUN apk --no-cache add cmake bash automake autoconf pcre-dev bison  
  
# number of concurrent threads during build  
# usage: docker build --build-arg PARALLELISM=8 -t name/name .  
ARG PARALLELISM=1  
ENV IROHA_HOME /tmp/iroha  
ENV IROHA_BUILD /tmp/iroha/build  
  
# install boost 1.65.1  
RUN git clone https://github.com/boostorg/boost /tmp/boost; \  
(cd /tmp/boost ; git checkout 436ad1dfcfc7e0246141beddd11c8a4e9c10b146); \  
(cd /tmp/boost ; git submodule init); \  
(cd /tmp/boost ; git submodule update --recursive -j ${PARALLELISM}); \  
(cd /tmp/boost ; /tmp/boost/bootstrap.sh --with-libraries=system,filesystem);
\  
(cd /tmp/boost ; /tmp/boost/b2 headers); \  
(cd /tmp/boost ; /tmp/boost/b2 cxxflags="-std=c++14" -j ${PARALLELISM}
install); \  
rm -rf /tmp/boost; \  
ln -s /usr/local/include/boost /usr/include/boost  
  
# install protobuf  
RUN git clone https://github.com/google/protobuf /tmp/protobuf; \  
(cd /tmp/protobuf ; git checkout 80a37e0782d2d702d52234b62dd4b9ec74fd2c95); \  
cmake -Dprotobuf_BUILD_TESTS=OFF -Dprotobuf_BUILD_SHARED_LIBS=ON
-H/tmp/protobuf/cmake -B/tmp/protobuf/.build; \  
cmake --build /tmp/protobuf/.build --target install -- -j${PARALLELISM}; \  
ldconfig; \  
rm -rf /tmp/protobuf  
  
# install c-ares  
RUN git clone https://github.com/c-ares/c-ares /tmp/c-ares; \  
(cd /tmp/c-ares ; git checkout 3be1924221e1326df520f8498d704a5c4c8d0cce); \  
cmake -H/tmp/c-ares -B/tmp/c-ares/build; \  
cmake --build /tmp/c-ares/build --target install -- -j${PARALLELISM}; \  
ldconfig; \  
rm -rf /tmp/c-ares  
  
# needed by grpc reference to libprotoc.so  
ENV LD_LIBRARY_PATH /usr/local/lib64  
  
# install grpc  
RUN git clone https://github.com/grpc/grpc /tmp/grpc; \  
(cd /tmp/grpc ; git checkout bfcbad3b86c7912968dc8e64f2121c920dad4dfb); \  
(cd /tmp/grpc ; git submodule update --init third_party/benchmark); \  
cmake -DgRPC_ZLIB_PROVIDER=package -DgRPC_CARES_PROVIDER=package
-DgRPC_SSL_PROVIDER=package \  
-DgRPC_PROTOBUF_PROVIDER=package -DgRPC_GFLAGS_PROVIDER=package -DBUILD_SHARED_LIBS=ON -H/tmp/grpc -B/tmp/grpc/.build; \  
cmake --build /tmp/grpc/.build --target install -- -j${PARALLELISM}; \  
ldconfig; \  
rm -rf /tmp/grpc  
  
# install ed25519  
RUN git clone git://github.com/hyperledger/iroha-ed25519.git /tmp/ed25519; \  
(cd /tmp/ed25519 ; git checkout e7188b8393dbe5ac54378610d53630bd4a180038); \  
cmake -DCMAKE_BUILD_TYPE=Debug -DTESTING=OFF -H/tmp/ed25519
-B/tmp/ed25519/build; \  
cmake --build /tmp/ed25519/build --target install -- -j${PARALLELISM}; \  
ldconfig; \  
rm -rf /tmp/ed25519  
  
# install swig  
RUN git clone https://github.com/swig/swig.git /tmp/swig; \  
(cd /tmp/swig ; git checkout fbeb566014a1d320df972aef965daf042db7db36); \  
(cd /tmp/swig ; ./autogen.sh && ./configure && make && make install); \  
ldconfig; \  
rm -rf /tmp/swig; \  
ln -s /usr/local/bin/swig /usr/bin/swig  
  
# install spdlog v0.16.3  
RUN git clone https://github.com/gabime/spdlog /tmp/spdlog; \  
(cd /tmp/spdlog ; git checkout ccd675a286f457068ee8c823f8207f13c2325b26); \  
cmake -DSPDLOG_BUILD_TESTING=OFF -H/tmp/spdlog -B/tmp/spdlog/build; \  
cmake --build /tmp/spdlog/build --target install; \  
rm -rf /tmp/spdlog  
  
# install shared_model of iroha  
RUN git clone https://github.com/hyperledger/iroha.git /tmp/iroha; \  
(cd /tmp/iroha ; git checkout develop); \  
(cd /tmp/iroha/schema ; python -m grpc_tools.protoc -I=./ --python_out=./
--grpc_python_out=./ ./*.proto ; mv *_pb*.py /usr/local/lib/python2.7); \  
rm -rf /tmp/iroha  
  
USER root

