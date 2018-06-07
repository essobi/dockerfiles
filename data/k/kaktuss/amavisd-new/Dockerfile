FROM alpine:3.5  
ENV CONSUL_TEMPLATE_VERSION=0.18.0  
COPY consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS
/usr/local/bin/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS  
  
RUN \  
apk add --update-cache amavisd-new spamassassin curl \  
perl-net-cidr-lite razor perl-mail-spf make unzip p7zip \  
  
&& curl -L https://cpanmin.us | perl - App::cpanminus \  
&& cpanm Image::Info \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& sha256sum -c consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
  
&& sa-update \  
  
&& apk del unzip && rm -rf /var/cache/apk/*  
  
COPY amavisd.conf.template /root/amavisd.conf.template  
COPY amavis.hcl /etc/amavis.hcl  
COPY amavis_start.sh /usr/local/bin/amavis_start.sh  
COPY sa-update /etc/periodic/daily/sa-update  
  
ENV AMAVIS_MYDOMAIN=  
ENV AMAVIS_ADMIN_USER=  
ENV AMAVIS_SERVICE=  
  
CMD /usr/local/bin/amavis_start.sh  

