FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
libmicrohttpd10 \  
libhwloc-dev \  
libssl1.0.0 \  
&& rm -r /var/lib/apt/lists/*  
  
ENV XMR_STAK_CPU_VERSION 2.4.4  
RUN set -x \  
&& buildDeps=' \  
ca-certificates \  
cmake \  
curl \  
g++ \  
libmicrohttpd-dev \  
libssl-dev \  
make \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& mkdir -p /usr/local/src/xmr-stak-cpu/build \  
&& cd /usr/local/src/xmr-stak-cpu/ \  
&& curl -sL https://github.com/IndeedMiners/xmr-aeon-
stak/archive/$XMR_STAK_CPU_VERSION.tar.gz | tar -xz --strip-components=1 \  
&& sed -i 's/constexpr double fDevDonationLevel.*/constexpr double
fDevDonationLevel = 0.0;/' xmrstak/donate-level.hpp \  
&& cd build \  
&& cmake -DOpenCL_ENABLE=OFF -DCUDA_ENABLE=OFF .. \  
&& make install -j$(nproc) \  
&& cp bin/xmr-stak /usr/local/bin/ \  
&& apt-get -qq --auto-remove purge $buildDeps  
  
COPY config.txt /config.txt  
COPY cpu.txt /cpu.txt  
COPY pools.txt /pools.txt  
  
ENTRYPOINT ["xmr-stak"]  

