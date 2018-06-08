FROM alpine:3.7 as protoc_builder  
RUN apk add --no-cache build-base curl automake autoconf libtool git zlib-dev  
  
ENV GRPC_VERSION=1.8.4 \  
PROTOBUF_VERSION=3.5.1 \  
OUTDIR=/out  
RUN mkdir -p /protobuf && \  
curl -L https://github.com/google/protobuf/archive/v${PROTOBUF_VERSION}.tar.gz
| tar xvz --strip-components=1 -C /protobuf  
RUN git clone \--depth 1 --recursive -b v${GRPC_VERSION}
https://github.com/grpc/grpc.git /grpc && \  
rm -rf grpc/third_party/protobuf && \  
ln -s /protobuf /grpc/third_party/protobuf  
RUN cd /protobuf && \  
autoreconf -f -i -Wall,no-obsolete && \  
./configure --prefix=/usr --enable-static=no && \  
make -j2 && make install  
RUN cd grpc && \  
make -j2 plugins  
RUN cd /protobuf && \  
make install DESTDIR=${OUTDIR}  
RUN cd /grpc && \  
make install-plugins prefix=${OUTDIR}/usr  
RUN find ${OUTDIR} -name "*.a" -delete -or -name "*.la" -delete  
  
FROM swift:4.0.3 as swift_builder  
  
# Install dependency library  
RUN apt-get update && \  
apt-get install -y automake libtool autoconf tzdata curl libcurl4-openssl-dev
patchelf && \  
apt-get clean  
  
# Build and install the swiftgrpc plugin  
RUN git clone -b dev https://github.com/novi/grpc-swift && \  
cd grpc-swift && \  
make all && \  
cp .build/debug/protoc-gen-swift /usr/bin && \  
cp .build/debug/protoc-gen-swiftgrpc /usr/bin  
RUN git clone https://github.com/saga-dash/swift-protobuf-validator && \  
cd swift-protobuf-validator && \  
make && \  
cp .build/debug/protoc-gen-swiftvalidator /usr/bin  
  
RUN mkdir -p /protoc-gen-swift && \  
cp /grpc-swift/.build/debug/protoc-gen-swift /protoc-gen-swift/ && \  
cp /grpc-swift/.build/debug/protoc-gen-swiftgrpc /protoc-gen-swift/ && \  
cp /swift-protobuf-validator/.build/debug/protoc-gen-swiftvalidator /protoc-
gen-swift/  
RUN cp /lib64/ld-linux-x86-64.so.2 \  
$(ldd /protoc-gen-swift/protoc-gen-swift | awk '{print $3}' | grep /lib | sort
| uniq) \  
/protoc-gen-swift/  
RUN find /protoc-gen-swift/ -name 'lib*.so*' -exec patchelf --set-rpath
/protoc-gen-swift {} \; && \  
for p in protoc-gen-swift protoc-gen-swiftgrpc protoc-gen-swiftvalidator; do \  
patchelf --set-interpreter /protoc-gen-swift/ld-linux-x86-64.so.2 /protoc-gen-
swift/${p}; \  
done  
  
FROM znly/upx as packer  
COPY \--from=protoc_builder /out/ /out/  
RUN upx --lzma \  
/out/usr/bin/protoc  
  
FROM alpine:3.7  
RUN apk add --no-cache libstdc++  
COPY \--from=packer /out/ /  
COPY \--from=swift_builder /protoc-gen-swift /protoc-gen-swift  
RUN for p in protoc-gen-swift protoc-gen-swiftgrpc protoc-gen-swiftvalidator;
do \  
ln -s /protoc-gen-swift/${p} /usr/bin/${p}; \  
done  
  
RUN apk add --no-cache curl && \  
mkdir -p /protobuf/google/protobuf && \  
for f in any duration descriptor empty struct timestamp wrappers; do \  
curl -L -o /protobuf/google/protobuf/${f}.proto
https://raw.githubusercontent.com/google/protobuf/master/src/google/protobuf/${f}.proto;
\  
done && \  
mkdir -p /protobuf/google/api && \  
for f in annotations http; do \  
curl -L -o /protobuf/google/api/${f}.proto
https://raw.githubusercontent.com/grpc-ecosystem/grpc-
gateway/master/third_party/googleapis/google/api/${f}.proto; \  
done && \  
mkdir -p /protobuf/google/pubsub/v1 && \  
for f in pubsub; do \  
curl -L -o /protobuf/google/pubsub/v1/${f}.proto
https://raw.githubusercontent.com/googleapis/googleapis/master/google/pubsub/v1/${f}.proto;
\  
done && \  
mkdir -p /protobuf/google/pubsub/v1beta2 && \  
for f in pubsub; do \  
curl -L -o /protobuf/google/pubsub/v1beta2/${f}.proto
https://raw.githubusercontent.com/googleapis/googleapis/master/google/pubsub/v1beta2/${f}.proto;
\  
done && \  
apk del curl  
  
ENTRYPOINT ["/usr/bin/protoc", "-I/protobuf"]  

