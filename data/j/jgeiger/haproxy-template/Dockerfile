FROM jgeiger/alpine  
MAINTAINER jgeiger@gmail.com  
  
EXPOSE 443 8080  
WORKDIR /tmp  
  
ENV CONSUL_TEMPLATE_VERSION=0.13.0  
RUN addgroup -S haproxy && adduser -S -G haproxy haproxy \  
&& apk add --update \  
curl \  
haproxy \  
&& curl -o /tmp/consul_template.zip -sSL
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& unzip /tmp/consul_template.zip \  
&& mv consul-template /usr/bin \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& apk del \  
curl \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
VOLUME ["/config"]  
  
ENTRYPOINT [ "tini", "--" ]  
  
CMD [ "consul-template", "-config=/config/haproxy.json" ]  

