FROM alpine:3.3  
MAINTAINER Allan Lei <allanlei@helveticode.com>  
  
ENV VERSION 1.79  
RUN apk --no-cache add --virtual .builddeps \  
build-base \  
automake \  
autoconf \  
fuse-dev \  
curl-dev \  
libxml2-dev \  
openssl-dev  
  
COPY src/s3fs-fuse /src/s3fs-fuse  
RUN cd /src/s3fs-fuse && \  
./autogen.sh && \  
./configure --with-openssl && \  
make && \  
make install && \  
apk --no-cache add \  
libstdc++ curl fuse libxml2 && \  
apk del .builddeps && \  
rm -rf /src/s3fs-fuse  
COPY entrypoint.sh /  
RUN mkdir -p /tmp /mnt && \  
chmod +x /entrypoint.sh  
VOLUME ["/mnt"]  
ENTRYPOINT ["/entrypoint.sh"]  

