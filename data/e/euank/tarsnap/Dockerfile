# Fedora 27 on 2018-04-05  
FROM
fedora@sha256:ec588fc80b05e19d3006bf2e8aa325f0a2e2ff1f609b7afb39176ca8e3e13467
as builder  
  
ENV VERSION=1.0.39  
RUN dnf install -y gcc make glibc-devel openssl-devel zlib-devel e2fsprogs-
devel  
  
RUN mkdir -p /work/build  
WORKDIR /work/build  
  
RUN curl -s -o /work/build/tarsnap-autoconf-${VERSION}.tgz
https://www.tarsnap.com/download/tarsnap-autoconf-${VERSION}.tgz  
RUN curl -s -o /work/build/tarsnap-sig.asc
https://www.tarsnap.com/download/tarsnap-sigs-${VERSION}.asc  
RUN curl -s https://www.tarsnap.com/tarsnap-signing-key-2018.asc | gpg2
--import  
RUN gpg2 --list-key 0xE19C439D5C002410 # verify we have the right key  
  
RUN gpg2 --decrypt tarsnap-sig.asc > SHA256SUMS  
RUN sha256sum -c SHA256SUMS  
  
RUN tar xvf tarsnap-autoconf-${VERSION}.tgz  
  
RUN cd tarsnap-autoconf-${VERSION} && ./configure && make all && make install  
  
RUN cp /usr/local/etc/tarsnap.conf.sample /usr/local/etc/tarsnap.conf  
  
VOLUME "/usr/local/tarsnap-cache"  
  
CMD /usr/local/bin/tarsnap  

