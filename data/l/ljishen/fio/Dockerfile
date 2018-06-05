FROM alpine:3.7  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
ARG VERSION=3.6  
ARG FOLDER_NAME=fio-fio-"$VERSION"  
RUN apk --no-cache add libaio && \  
apk --no-cache add --virtual build-dependencies \  
libaio-dev \  
zlib-dev \  
build-base \  
linux-headers \  
coreutils && \  
wget -c https://codeload.github.com/axboe/fio/tar.gz/fio-"$VERSION" -O - | tar
-xz -C /root && \  
cd /root/"$FOLDER_NAME" && \  
./configure && \  
make -j "$(nproc)" && \  
make install && \  
rm -rf /root/"$FOLDER_NAME" && \  
apk del build-dependencies  
  
ENTRYPOINT ["fio"]  

