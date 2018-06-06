#  
# This is a multi-stage build.  
# Actual build is at the very end.  
#  
FROM library/ubuntu:xenial AS build  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y \  
python-software-properties \  
software-properties-common \  
apt-utils  
RUN apt-get install -y \  
wget  
  
RUN mkdir -p /build/image  
WORKDIR /build  
RUN wget
http://delegate.hpcc.jp/anonftp/DeleGate/bin/linux/9.9.13/linux2.6-dg9_9_13.tar.gz
&& \  
tar -xvf linux2.6-dg9_9_13.tar.gz  
RUN apt-get download \  
ca-certificates \  
libstdc++6 \  
zlib1g \  
libssl1.0.0  
RUN for file in *.deb; do dpkg-deb -x ${file} image/; done  
  
WORKDIR /build/image  
RUN rm -rf \  
etc/ca-certificates \  
usr/sbin \  
usr/share/man \  
usr/share/gdb \  
usr/share/gcc-5 \  
usr/share/doc && \  
mkdir -p \  
usr/bin \  
var/lib/delegate \  
var/spool/delegate \  
var/run/delegate \  
var/cache/delegate \  
var/log/delegate \  
etc/delegate && \  
cat usr/share/ca-certificates/mozilla/*.crt > etc/ssl/certs/ca-
certificates.crt && \  
cp ../dg9_9_13/DGROOT/bin/dg9_9_13 usr/bin/delegated && \  
touch etc/delegate.conf  
  
FROM clover/base  
  
ENV DGROOT /var/lib/delegate  
ENV VARDIR /var/spool/delegate  
ENV CACHEDIR /var/cache/delegate  
ENV ETCDIR /etc/delegate  
ENV LOGDIR /var/log/delegate  
ENV ACTDIR /var/spool/act  
ENV TMPDIR /tmp  
ENV PIDDIR /var/run/delegate  
ENV OWNER root/root  
  
WORKDIR /  
COPY \--from=build /build/image /  
  
CMD ["delegated", "-f", "+=/etc/delegate.conf"]  

