FROM alpine:3.4  
MAINTAINER Ali Farhadi <a.farhadi@gmail.com>  
  
COPY emqtt.ini /etc/supervisor.d/emqtt.ini  
  
RUN apk --no-cache add erlang supervisor \  
&& apk add --no-cache --virtual=build-dependencies perl wget git make erlang-
dev erlang-syntax-tools erlang-eunit erlang-crypto erlang-reltool erlang-asn1
erlang-tools erlang-eldap erlang-inets erlang-mnesia erlang-observer erlang-
os-mon erlang-public-key erlang-runtime-tools erlang-sasl erlang-ssl erlang-
xmerl \  
&& git clone https://github.com/emqtt/emqttd-relx /emqttd \  
&& cd /emqttd \  
&& make \  
&& mkdir /opt \  
&& mv /emqttd/_rel/emqttd /opt/emqttd \  
&& apk --purge del build-dependencies \  
&& cd / && rm -rf /emqttd  
  
ENV PATH=$PATH:/opt/emqttd/bin  
  
WORKDIR /opt/emqttd  
  
VOLUME ["/opt/emqttd/etc", "/opt/emqttd/data", "/opt/emqttd/log"]  
  
# 1883 port for MQTT, 8883 port for MQTTS(SSL), 8083 for WebSocket/HTTP, 18083
for dashboard  
EXPOSE 1883 8883 8083 18083  
CMD ["/usr/bin/supervisord"]  

