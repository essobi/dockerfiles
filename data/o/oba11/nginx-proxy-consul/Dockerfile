FROM alpine  
MAINTAINER Oluwaseun Obajobi <oba@obajobi.com>  
  
RUN apk add --update nginx openssl && rm -rf /var/cache/apk/*  
  
ENV CONSUL_TEMPLATE_VERSION 0.9.0  
RUN wget -P /tmp https://github.com/hashicorp/consul-
template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz && \  
tar -C /tmp -xvzf /tmp/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz && \  
mv /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64/consul-template
/bin/consul-template && \  
rm -rf /tmp/*  
  
ADD ./proxy_params /etc/nginx/proxy_params  
ADD ./config /config  
ADD ./nginx.conf /etc/nginx/nginx.conf  
  
RUN chmod u+x /config/start.sh  
  
WORKDIR /config  
EXPOSE 80 443  
CMD ["/config/start.sh"]  

