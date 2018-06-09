FROM ubuntu:17.04  
  
MAINTAINER Stefan Rohe <think@hotmail.de>  
  
RUN apt-get update -y \  
&& apt-get install -y \  
binutils \  
curl \  
g++ \  
gcc \  
git \  
libz-dev \  
llvm-3.9-dev \  
llvm-3.9-runtime \  
make \  
nasm \  
xz-utils \  
&& curl -fsS https://dlang.org/install.sh | bash -s dmd \  
&& git clone https://github.com/SDC-Developers/SDC.git \  
&& . ~/dlang/dmd-*/activate && cd SDC && make LLVM_CONFIG=llvm-config-3.9 \  
&& apt-get auto-remove -y \  
curl \  
git \  
g++ \  
libz-dev \  
llvm-3.9-dev \  
make \  
nasm \  
xz-utils \  
&& rm -rf \  
/SDC/.git \  
/root/dlang/dmd-*/html \  
/root/dlang/dmd-*/linux/{bin,lib}32 \  
/root/dlang/dub*/dub.tar.gz \  
/var/lib/apt/lists/*  
  
ENV \  
LD_LIBRARY_PATH=/root/dlang/dmd-2.073.0/linux/lib64 \  
PATH=/SDC/bin:/root/dlang/dub:/root/dlang/dmd-2.073.0/linux/bin64:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
WORKDIR /src  
  
ENV GOSU_VERSION 1.9  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget \  
&& wget -O /usr/local/bin/gosu \  
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc \  
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture).asc" \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get auto-remove -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
CMD ["sdc"]  

