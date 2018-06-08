FROM alpine:3.4  
MAINTAINER Maxim Zalysin <zalysin.m@gmail.com>  
  
LABEL pro.magnaz.docker.powerdns.version="{\"container\": 1.6, \"alpine\":
3.4, \"powerdns\": 4.0.1}"  
  
RUN export POWERDNS_VERSION=4.0.1 && \  
apk --no-cache add boost-dev mariadb-client-libs && \  
apk --no-cache add --virtual build-dependencies g++ make mariadb-dev curl && \  
curl -sSL
https://downloads.powerdns.com/releases/pdns-$POWERDNS_VERSION.tar.bz2 | tar
xjf - -C /tmp && \  
cd /tmp/pdns-$POWERDNS_VERSION && \  
./configure --prefix="" \--exec-prefix=/usr --sysconfdir=/etc/powerdns --with-
modules="gmysql" && \  
make && make install && \  
apk del build-dependencies && cd / && rm -rf /tmp/pdns-$POWERDNS_VERSION  
  
EXPOSE 53 53/udp 8081  
ENTRYPOINT ["pdns_server"]

