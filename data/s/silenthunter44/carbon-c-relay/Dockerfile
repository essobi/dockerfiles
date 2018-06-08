FROM debian:stretch-slim  
  
MAINTAINER Guillaume CONNAN "guillaume.connan44@gmail.com"  
  
LABEL version="0.3.4"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN ( \  
echo "deb http://deb.debian.org/debian stretch main contrib non-free" \  
> /etc/apt/sources.list && \  
echo "deb http://deb.debian.org/debian stretch-updates main contrib non-free"
\  
>> /etc/apt/sources.list && \  
echo "deb http://security.debian.org stretch/updates main contrib non-free" \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y -q upgrade && \  
apt-get -y -q dist-upgrade && \  
apt-get -y -q autoclean && \  
apt-get -y -q autoremove && \  
apt-get -y -q install build-essential git libssl-dev sudo zlib1g-dev && \  
git clone --quiet \  
https://github.com/grobian/carbon-c-relay.git \  
/carbon-c-relay && \  
( \  
cd /carbon-c-relay && \  
touch conffile.yy.c conffile.tab.c conffile.tab.h && \  
touch configure.ac Makefile.am aclocal.m4 configure \  
Makefile.in config.h.in && \  
export CC=gcc && \  
./configure --with-gzip --without-lz4 --with-ssl && \  
make CFLAGS="-O3 -Wall -Werror -Wshadow -pipe" \  
LIBS="-lcrypto -lpthread -lm" \  
) && \  
groupadd -g 1000 -r relay && \  
useradd -g relay -r -s /bin/false -u 1000 relay && \  
mv -f /carbon-c-relay/relay /usr/local/bin/ && \  
rm -fr /carbon-c-relay && \  
apt-get -y -q purge build-essential git libssl-dev zlib1g-dev && \  
apt-get -y -q autoremove && \  
apt-get clean && \  
rm -fr /tmp/* && \  
rm -fr /var/tmp/* && \  
rm -fr /var/lib/apt/lists/* \  
)  
  
COPY run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
  
USER root  
EXPOSE 2003 2003/udp  
VOLUME ["/carbon-c-relay"]  
CMD ["run.sh"]  

