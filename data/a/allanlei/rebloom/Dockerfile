FROM redis:32bit as builder  
  
ARG VERSION=1.0.0  
WORKDIR /  
RUN apt-get update && \  
apt-get install -y \  
curl \  
gcc \  
gcc-multilib \  
libc6-dev-i386 \  
make  
RUN curl -sfL
https://github.com/RedisLabsModules/rebloom/archive/v$VERSION.tar.gz | tar xz
-C /  
RUN export "CFLAGS=-m32" "SHOBJ_LDFLAGS=-m elf_i386 -shared -Bsymbolic
-Bsymbolic-functions" && \  
make -C rebloom-$VERSION  
  
###  
FROM busybox  
  
ARG VERSION=1.0.0  
ENV LIBDIR /var/lib/redis/modules  
WORKDIR $LIBDIR  
VOLUME $LIBDIR  
COPY \--from=builder /rebloom-$VERSION/rebloom.so $LIBDIR/rebloom.so  

