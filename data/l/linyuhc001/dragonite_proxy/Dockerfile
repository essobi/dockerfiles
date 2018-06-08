FROM alpine:3.6  
ARG TZ='Asia/Shanghai'  
ENV TZ $TZ  
ENV SS_LIBEV_VERSION 3.1.0  
RUN apk upgrade --update \  
&& apk add bash tzdata libsodium openjdk8-jre-base\  
curl \  
tar \  
git \  
&& curl -sSLO https://github.com/dragonite-network/dragonite-
java/releases/download/fwd-0.3.3-prx-0.3.1/dragonite-proxy-0.3.1.tar \  
&& mkdir /dragonite \  
&& tar -xvf dragonite-proxy-0.3.1.tar -C /dragonite \  
&& chmod +x /dragonite/dragonite-proxy-0.3.1/bin/dragonite-proxy \  
&& ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone \  
&& rm -rf dragonite-forwarder-0.3.3.tar \  
/var/cache/apk/*  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

