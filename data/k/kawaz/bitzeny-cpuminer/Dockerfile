FROM ubuntu:17.04 AS BUILD  
RUN apt-get update  
RUN apt-get install -y git automake autoconf pkg-config libcurl4-openssl-dev
libjansson-dev libssl-dev libgmp-dev make g++  
  
WORKDIR /build  
RUN git clone \--depth 1 https://github.com/bitzeny/cpuminer.git  
RUN cd cpuminer && \  
./autogen.sh && \  
./configure CFLAGS="-O3 -march=native -funroll-loops -fomit-frame-pointer" &&
\  
make  
RUN \  
cp /build/cpuminer/minerd /usr/bin/minerd && \  
ldd /usr/bin/minerd | grep -Eo '/[^ ]+' > minerd.dep_ldd && \  
dpkg -S $(cat minerd.dep_ldd) | perl -pe's/:.*//' | sort -u >
minerd.dep_packages  
  
FROM ubuntu:17.04 AS MAIN  
COPY \--from=BUILD /usr/bin/minerd /usr/bin/  
COPY \--from=BUILD /build/minerd.dep_packages /  
RUN apt-get update && apt-get install -y inetutils-ping ca-certificates $(cat
/*.dep_packages) --no-install-recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /*.dep_packages  
ENV \  
ALGO=yescrypt \  
USER=kawazzz \  
WORKER=donation \  
USERNAME= \  
PASSWORD=x \  
POOL=stratum+tcp://jp.lapool.me:3014  
ADD bootstrap.sh bootstrap.sh  
ENTRYPOINT [ "./bootstrap.sh" ]  

