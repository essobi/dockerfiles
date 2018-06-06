FROM jean1989/debian-base  
  
ENV CLANG_VERSION="3.8" \  
NPM_VERSION="latest" \  
DEBIAN_FRONTEND="noninteractive"  
  
MAINTAINER Jean1989  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list.d/backports.list \  
&& echo "deb http://apt.llvm.org/jessie/ llvm-toolchain-
jessie-${CLANG_VERSION} main" >> /etc/apt/sources.list.d/llvm.list \  
&& wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \  
&& apt-get update \  
&& apt-get -t llvm-toolchain-jessie-$CLANG_VERSION install -y \--no-install-
recommends clang-$CLANG_VERSION lldb-$CLANG_VERSION \  
&& apt-get -t jessie-backports install -y \--no-install-recommends cmake \  
&& apt-get install -y \--force-yes \--no-install-recommends build-essential \  
llvm \  
libunwind-dev \  
libicu-dev \  
python \  
&& update-alternatives \--install /usr/bin/clang clang
/usr/bin/clang-$CLANG_VERSION 100 \  
&& update-alternatives \--install /usr/bin/clang++ clang++
/usr/bin/clang++-$CLANG_VERSION 100 \  
&& wget \--quiet -O "node-chakracore.tar.gz"
https://api.github.com/repos/nodejs/node-chakracore/tarball/xplat > /dev/null
2>&1 \  
&& tar -zxf node-chakracore.tar.gz \  
&& rm -rf node-chakracore.tar.gz \  
&& cd nodejs-node-chakracore-* \  
&& ./configure \--prefix=/usr \--engine=chakracore \--partly-static
\--download=all \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make -j${NPROC} \  
&& make install \  
&& paxctl -cm /usr/bin/node \  
&& cd ../ \  
&& rm -rf nodejs-node-chakracore-* \  
&& apt-get purge \--auto-remove -y llvm cmake build-essential
clang-$CLANG_VERSION lldb-$CLANG_VERSION python \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html \  
/var/lib/apt/lists/*  

