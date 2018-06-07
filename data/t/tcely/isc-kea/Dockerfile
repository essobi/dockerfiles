ARG BOTAN_VERSION=2.5.0  
FROM alpine AS builder  
  
ARG BOTAN_VERSION  
  
RUN apk --update upgrade && \  
apk add ca-certificates curl && \  
apk add --virtual .build-depends \  
file gnupg g++ make \  
boost-dev bzip2-dev libressl-dev sqlite-dev zlib-dev \  
binutils python3-dev && \  
curl -RL -O
"https://botan.randombit.net/releases/Botan-${BOTAN_VERSION}.tgz{.asc,}" && \  
mkdir -v -m 0700 -p /root/.gnupg && \  
gpg2 --no-options --verbose --keyserver-options auto-key-retrieve=true
\--keyid-format 0xlong --verify Botan-*.asc Botan-*.tgz && \  
rm -rf /root/.gnupg *.asc && \  
tar -xpf "Botan-${BOTAN_VERSION}.tgz" && \  
rm -f "Botan-${BOTAN_VERSION}.tgz" && \  
( \  
cd "Botan-${BOTAN_VERSION}" && \  
./configure.py --with-boost --with-bzip2 --with-openssl --with-sqlite3 --with-
zlib && \  
make -j 4 && \  
make install \  
) && \  
strip -p -s /usr/local/bin/botan && \  
apk del --purge .build-depends && rm -rf /var/cache/apk/*  
  
FROM alpine  
LABEL maintainer="https://keybase.io/tcely"  
  
RUN apk --update upgrade && \  
apk add ca-certificates curl less man \  
boost bzip2 libressl sqlite zlib \  
python3 && \  
rm -rf /var/cache/apk/*  
  
ENV PAGER less  
  
COPY \--from=builder /usr/local/bin/botan /usr/local/bin/botan  
COPY \--from=builder /usr/local/include/botan-2 /usr/local/include/botan-2/  
COPY \--from=builder /usr/local/lib /usr/local/lib/  
COPY \--from=builder /usr/local/share/doc /usr/local/share/doc/  
  
ENTRYPOINT ["/bin/ls"]  
CMD ["-alR", "/usr/local"]  

