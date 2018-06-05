FROM ubuntu:16.04  
MAINTAINER Jonathan Brooker <jonathan.brooker@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential wget rsync cmake pkg-config perl-modules \  
libdigest-md5-file-perl xz-utils python \  
clang clang-tidy clang-format git libstdc++-4.9-dev libssl-dev \  
liblmdb-dev gdb llvm locate \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& updatedb  
  
COPY . /home/quality  
WORKDIR /work/build  
ENTRYPOINT /home/quality/build.sh /work/source  

