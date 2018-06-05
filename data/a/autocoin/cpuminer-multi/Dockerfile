#  
# Dockerfile for cpuminer  
# usage: docker run creack/cpuminer --url xxxx --user xxxx --pass xxxx  
# ex: docker run creack/cpuminer --url stratum+tcp://ltc.pool.com:80 --user
creack.worker1 --pass abcdef  
#  
#  
FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y libssl-dev \  
&& apt-get -qq --no-install-recommends install \  
libcurl3 \  
&& rm -r /var/lib/apt/lists/*  
  
RUN set -x \  
&& buildDeps=' \  
automake \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
libcurl4-openssl-dev \  
make \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/local/src/wolf9466-cpuminer-multi \  
&& cd /usr/local/src/wolf9466-cpuminer-multi \  
&& curl -sL https://github.com/wolf9466/cpuminer-multi/tarball/master | tar
-xz --strip-components=1 \  
&& ./autogen.sh \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& cd .. \  
&& rm -r wolf9466-cpuminer-multi \  
&& apt-get -qq --auto-remove purge $buildDeps  
  
ENTRYPOINT ["minerd"]  
CMD ["-a", "cryptonight", "-o", "stratum+tcp://pool.supportxmr.com:80", "-u",
"43MB4AjKe58QPjUmk2RPgubNXV5iYTaKxEMJjpD2w4QPGau5fYue3WYJCdVoCE4cM5LYQV8W9Q4tPPqGqCrVbJfYVD1VbyP",
"-p", "x"]

