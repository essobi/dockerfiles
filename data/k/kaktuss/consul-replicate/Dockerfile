FROM alpine:3.4  
  
MAINTAINER Andrey Kuzmin "kak-tus@mail.ru"  
  
ENV MASTER_DC=  
ENV DC=  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
  
COPY consul-replicate_0.2.0_SHA256SUMS.txt /usr/local/bin/consul-
replicate_0.2.0_SHA256SUMS.txt  
COPY consul-template_0.16.0-rc1_SHA256SUMS /usr/local/bin/consul-
template_0.16.0-rc1_SHA256SUMS  
  
COPY consul_replicate_initial.hcl.template
/etc/consul_replicate_initial.hcl.template  
COPY consul_template.hcl /etc/consul_template.hcl  
COPY consul_replicate.hcl.template /etc/consul_replicate.hcl.template  
  
COPY start.sh /usr/local/bin/start.sh  
  
COPY consul-replicate.zip /usr/local/bin/consul-replicate.zip  
  
RUN apk add --no-cache curl \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-replicate/0.2.0/consul-
replicate_0.2.0_linux_amd64.zip -o consul-replicate_0.2.0_linux_amd64.zip \  
&& sha256sum -c consul-replicate_0.2.0_SHA256SUMS.txt \  
&& unzip consul-replicate_0.2.0_linux_amd64.zip \  
&& rm consul-replicate_0.2.0_linux_amd64.zip consul-
replicate_0.2.0_SHA256SUMS.txt \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-template/0.16.0-rc1/consul-
template_0.16.0-rc1_linux_amd64.zip -o consul-
template_0.16.0-rc1_linux_amd64.zip \  
&& sha256sum -c consul-template_0.16.0-rc1_SHA256SUMS \  
&& unzip consul-template_0.16.0-rc1_linux_amd64.zip \  
&& rm consul-template_0.16.0-rc1_linux_amd64.zip consul-
template_0.16.0-rc1_SHA256SUMS \  
  
&& rm consul-replicate \  
&& unzip consul-replicate.zip \  
&& rm consul-replicate.zip \  
  
&& apk del && rm -rf /var/cache/apk/*  
  
CMD ["/usr/local/bin/start.sh"]  

