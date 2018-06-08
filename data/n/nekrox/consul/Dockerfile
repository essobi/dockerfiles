FROM alpine:latest  
MAINTAINER Alvaro Lizama <hola@alvarolizama.net>  
  
RUN apk update \  
&& apk add --upgrade musl unzip openssl ca-certificates \  
&& cd /usr/local/bin \  
&& wget
https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip -O
consul.zip \  
&& unzip consul.zip \  
&& chmod +x /usr/local/bin/consul \  
&& rm -rf consul.zip \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/consul"]  

