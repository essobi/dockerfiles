FROM alpine  
  
MAINTAINER life2cloud lee_jianfeng@sjtu.edu.cn  
  
ENV version 0.7.15  
  
RUN apk add \--update \--no-cache ncurses \  
&& apk add \--virtual=deps \--update \--no-cache musl-dev zlib-dev make gcc
curl\  
&& cd /tmp \  
&& curl -fsSL https://github.com/lh3/bwa/archive/v${version}.tar.gz -o
v${version}.tar.gz \  
&& tar xzvf v${version}.tar.gz \  
&& cd /tmp/bwa-${version} \  
&& sed -i '1i#include <stdint.h>' kthread.c \  
&& sed -i[.bak] "s/u_int32_t/uint32_t/g" *.c \  
&& sed -i[.bak] "s/u_int32_t/uint32_t/g" *.h \  
&& make \  
&& mv /tmp/bwa-${version}/bwa /usr/bin/ \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& apk del deps  
  
ENTRYPOINT ["/usr/bin/bwa"]  

