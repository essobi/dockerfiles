# build stage  
FROM alpine:3.6 as builder  
  
# devel branch  
ARG UPX_COMMIT_HASH=HEAD  
ENV LDFLAGS=-static  
  
# download source and compile  
RUN apk add --no-cache \  
build-base \  
git \  
ucl-dev \  
zlib-dev \  
&& git clone -b devel --recursive https://github.com/upx/upx.git /upx \  
&& git -C /upx reset --hard "${UPX_COMMIT_HASH}" \  
&& sed -i 's/ -O2/ /' /upx/src/Makefile \  
&& make -j10 -C /upx/src upx.out CHECK_WHITESPACE=  
  
# compress himself; absolutley barbaric ;)  
RUN /upx/src/upx.out \  
\--lzma \  
-o /usr/bin/upx \  
/upx/src/upx.out  
  
# final stage  
FROM busybox:1.27.2  
ARG BUILD_DATE  
  
LABEL org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.schema-version="1.0"  
  
COPY \--from=builder /usr/bin/upx /usr/bin/upx  
  
ENTRYPOINT ["/usr/bin/upx"]  

