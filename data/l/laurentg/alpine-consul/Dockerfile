FROM alpine:3.6  
ENV S6_OVERLAY_VERSION=v1.19.1.1  
ENV GO_DNSMASQ_VERSION=1.0.7  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz /tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
  
ADD https://github.com/janeczku/go-
dnsmasq/releases/download/${GO_DNSMASQ_VERSION}/go-dnsmasq_linux-amd64
/usr/local/bin/go-dnsmasq  
RUN chmod +x /usr/local/bin/go-dnsmasq  
  
RUN apk add --update bash openssl unzip curl && \  
rm -rf /var/cache/apk/*  
  
ADD rootfs /  
  
ENV CONSUL_VERSION=1.0.6  
RUN cd /tmp && \  
curl -O
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
cd /usr/local/bin && \  
unzip /tmp/consul_${CONSUL_VERSION}_linux_amd64.zip && \  
mkdir -p /etc/consul && \  
mkdir -p /var/consul && \  
addgroup consul && \  
adduser -D -s /bin/bash -g consul -G consul consul && \  
chown -R consul:consul /var/consul /etc/consul && \  
rm -fr /tmp/*  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 53 53/udp  
  
ENTRYPOINT ["/init"]  
  
VOLUME /var/consul  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/loicalbertin/docker-consul.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1"  
  

