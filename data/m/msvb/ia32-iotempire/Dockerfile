#FROM 32bit/ubuntu  
FROM ubuntu  
  
# install intermediate dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y curl unzip  
  
# install build dependencies  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y autoconf automake libtool make  
  
# install networking requirements  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y telnet traceroute iputils-ping avahi-utils  
  
# install development requirements  
RUN apt-get install -y gcc nodejs nodejs-legacy npm  
  
# install IoT requirements  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
rabbitmq-server \  
mosquitto-clients \  
mosquitto \  
libzmq-dev  
  
# install tools and utilities  
RUN apt-get install -y vim openssh-client  
  
# define local environment  
ENV LIBCOAP_VERSION 4.1.1  
# fetch manual builds  
#RUN curl -SLO "https://github.com/obgm/libcoap/archive/master.zip" \  
#RUN curl -SLO "https://github.com/obgm/libcoap/archive/develop.zip" \  
RUN curl -SLO "https://github.com/obgm/libcoap/archive/v$LIBCOAP_VERSION.zip"
\  
&& curl -SLO https://raw.githubusercontent.com/obgm/libcoap/develop/autogen.sh
\  
&& unzip "v$LIBCOAP_VERSION.zip" \  
&& chmod +x autogen.sh \  
&& mv autogen.sh "libcoap-$LIBCOAP_VERSION"/  
  
# install manual builds  
RUN cd "libcoap-$LIBCOAP_VERSION" \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& mv libcoap.a /usr/local/lib/ \  
&& mv examples/coap-* /usr/local/bin/ \  
&& cd ..  
  
# clean up post build environment  
RUN rm -rf "libcoap-$LIBCOAP_VERSION" "v$LIBCOAP_VERSION.zip"  
  
## install education environment  
#RUN npm install -g workshopper  
# configure development environment  
RUN npm install -g amqp mqtt zmq  
  
# add a standard development user (iotisgreat1234)  
RUN useradd -m -c 'IoT User' -s /bin/bash -u 1234 -U -p
'$6$W32qzUGv$kVCdAX2fHaDbCGVyQ538erbTVca2XxcR8ZHzcXFLfA2zmXRx8EvVkYD5uE8MZQOLyo9PRUSbl4n6NmZe28yf3/'
iotuser  
  
# conclude image build and container bootstrap  
CMD [ "echo", "Welcome to Building an IoT Empire" ]  

