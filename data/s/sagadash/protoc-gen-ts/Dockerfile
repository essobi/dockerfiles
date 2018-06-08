FROM alpine:3.6 as protoc_builder  
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
  
FROM znly/upx as packer  
COPY \--from=protoc_builder /out/ /out/  
RUN upx --lzma \  
/out/usr/bin/protoc \  
/out/usr/bin/grpc_*  
  
FROM node:alpine  
RUN apk add --no-cache libstdc++  
COPY \--from=packer /out/ /  
  
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
apk del curl  
  
RUN npm install -g ts-protoc-gen  
  
ENTRYPOINT ["/usr/bin/protoc", "-I/protobuf"]  

