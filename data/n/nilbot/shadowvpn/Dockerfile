#  
# Dockerfile for ShadowVPN  
#  
  
FROM alpine  
MAINTAINER nilbot <help@nilbot.net>  
  
RUN apk add -U autoconf \  
automake \  
build-base \  
gawk \  
git \  
iptables \  
libtool \  
linux-headers \  
&& git clone --recursive https://github.com/vimagick/ShadowVPN.git \  
&& cd ShadowVPN \  
&& ./autogen.sh \  
&& ./configure --enable-static --sysconfdir=/etc \  
&& make install \  
&& cd .. \  
&& rm -rf ShadowVPN \  
&& apk del autoconf \  
automake \  
build-base \  
gawk \  
git \  
libtool \  
linux-headers  
  
EXPOSE 53/udp  
  
CMD shadowvpn -c /etc/shadowvpn/server.conf  

