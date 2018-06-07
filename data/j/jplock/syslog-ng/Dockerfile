# DOCKER-VERSION 1.1.2  
# VERSION 0.1  
FROM debian:jessie  
MAINTAINER Justin Plock <justin@plock.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -q wget bison pkg-config \  
libevtlog-dev libevtlog0 libivykis0 libnet1 libglib2.0-dev \  
libjson-c-dev git dh-autoreconf librdkafka-dev  
  
RUN wget -q -O - https://github.com/balabit/syslog-
ng/releases/download/v3.5.5/syslog-ng-3.5.5.tar.gz | tar -xzf - -C /opt  
WORKDIR /opt/syslog-ng-3.5.5  
RUN ./configure --prefix=/usr/local \--enable-json --disable-stomp \  
\--disable-redis --disable-smtp --disable-amqp --disable-mongodb \  
\--without-libmongo-client --without-librabbitmq-client  
RUN make && make install  
  
WORKDIR /opt  
RUN git clone https://github.com/balabit/syslog-ng-incubator.git  
WORKDIR /opt/syslog-ng-incubator  
RUN autoreconf -i  
RUN ./configure --prefix=/usr/local \--enable-kafka  
RUN make && make install  
RUN ldconfig  
  
EXPOSE 514/tcp 514/udp  
  
ENTRYPOINT ["/usr/local/sbin/syslog-ng"]  
CMD ["--help"]  

