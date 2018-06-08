FROM ubuntu:16.04  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
\--no-install-suggests \  
autoconf \  
automake \  
bison \  
build-essential \  
ca-certificates \  
clang \  
llvm-dev \  
g++ \  
gcc \  
git \  
libtool \  
libtool-bin \  
libglib2.0-dev \  
make \  
nasm \  
wget \  
&& cd /usr/local/src \  
&& wget 'http://lcamtuf.coredump.cx/afl/releases/afl-2.52b.tgz' -O- | tar zxvf
- \  
&& cd afl-* \  
&& sed -rie
's/^(#[[:space:]]*define[[:space:]]+KEEP_UNIQUE_CRASH[[:space:]]+).*$/\120000/'
config.h \  
&& sed -rie
's/^(#[[:space:]]*define[[:space:]]+KEEP_UNIQUE_HANG[[:space:]]+).*$/\120000/'
config.h \  
&& sed -rie
's/^(#[[:space:]]*define[[:space:]]+PLOT_UPDATE_SEC[[:space:]]+).*$/\1900/'
config.h \  
&& sed -rie
's/^(#[[:space:]]*define[[:space:]]+STATS_UPDATE_SEC[[:space:]]+).*$/\1900/'
config.h \  
&& sed -rie
's/^(#[[:space:]]*define[[:space:]]+UI_TARGET_HZ[[:space:]]+).*$/\11/'
config.h \  
&& sed -rie 's/^(#[[:space:]]*define[[:space:]]+USE_COLOR.*$)/\/* \1 *\//'
config.h \  
&& make \  
&& cd llvm_mode \  
&& make \  
&& cd ../qemu_mode \  
&& ./build_qemu_support.sh \  
&& cd ../libdislocator \  
&& make \  
&& cd ../libtokencap \  
&& make \  
&& cd .. \  
&& make install \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  

