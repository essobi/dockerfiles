FROM alpine:latest  
LABEL maintainer "koshatul@gmail.com"  
  
RUN apk add --no-cache git make gcc libc-dev autoconf automake libtool vim bc
coreutils  
  
WORKDIR /bench  
  
## Sysbench  
RUN git clone \--depth 1 https://github.com/akopytov/sysbench.git sysbench  
RUN ( \  
cd /bench/sysbench/third_party/concurrency_kit/ck; \  
./configure; \  
make install \  
)  
RUN ( \  
cd /bench/sysbench; \  
./autogen.sh && \  
./configure --without-mysql --without-pgsql --without-oracle && \  
make \  
)  
  
## MBW from github  
RUN git clone \--depth 1 https://github.com/raas/mbw.git mbw  
RUN ( cd /bench/mbw; make )  
  
COPY bench /bench  
COPY init.sh /init.sh  
  
# RUN apt-get update && \  
# apt-get install -y mbw sysbench phoronix-test-suite && \  
# rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["/init.sh"]  

