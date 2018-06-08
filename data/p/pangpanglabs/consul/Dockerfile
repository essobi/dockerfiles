FROM alpine:latest  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ENV CONSUL_VERSION 0.7.5  
ENV CONSUL_SHA256
40ce7175535551882ecdff21fdd276cef6eaab96be8a8260e0599fadb6f1f5b8  
ENV CONSUL_WEBUI_SHA256
a7803e7ba2872035a7e1db35c8a2186ad238bf0f90eb441ee4663a872b598af4  
  
# install consul  
RUN apk --no-cache add curl ca-certificates \  
&& curl -sSL
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
-o /tmp/consul.zip \  
&& echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& cd /bin \  
&& unzip /tmp/consul.zip \  
&& chmod +x /bin/consul \  
&& rm /tmp/consul.zip  
  
# install consul web-ui  
RUN apk --no-cache add curl ca-certificates \  
&& curl -sSL
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
-o /tmp/webui.zip \  
&& echo "${CONSUL_WEBUI_SHA256} /tmp/webui.zip" > /tmp/consul_webui.sha256 \  
&& sha256sum -c /tmp/consul_webui.sha256 \  
&& mkdir /ui \  
&& cd /ui \  
&& unzip /tmp/webui.zip \  
&& rm /tmp/webui.zip  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
ENV DNS_RESOLVES consul  
ENV DNS_PORT 8600  
VOLUME /config  
  
ENTRYPOINT ["/bin/consul", "agent", "-config-dir=/config"]

