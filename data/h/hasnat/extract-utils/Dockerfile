FROM alpine as builder  
  
RUN apk add --update wget tar g++ make xz perl  
  
# From https://github.com/atdt/advcpmv  
RUN cd /root && wget http://ftp.gnu.org/gnu/coreutils/coreutils-8.25.tar.xz \  
&& tar xvJf coreutils-8.25.tar.xz \  
&& cd coreutils-8.25/ \  
&& wget
https://raw.githubusercontent.com/atdt/advcpmv/master/advcpmv-0.7-8.25.patch \  
&& patch -p1 -i advcpmv-0.7-8.25.patch \  
&& FORCE_UNSAFE_CONFIGURE=1 ./configure \  
&& make  
  
  
FROM alpine  
  
RUN apk add --update --no-cache tar unzip pv xz libarchive-tools  
COPY \--from=builder /root/coreutils-8.25/src/cp /usr/local/bin/cpg  
COPY \--from=builder /root/coreutils-8.25/src/mv /usr/local/bin/mvg  

