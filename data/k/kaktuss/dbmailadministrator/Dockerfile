FROM alpine:3.6  
ENV CONSUL_TEMPLATE_VERSION=0.18.5  
ENV
CONSUL_TEMPLATE_SHA256=b0cd6e821d6150c9a0166681072c12e906ed549ef4588f73ed58c9d834295cd2  
  
ENV DBMA_VERSION=3  
ENV
DBMA_SHA256=629172c54ff00d4a2cb2f4f250f93373d31eba995f601794abe5894731fca09d  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
curl \  
unzip \  
  
&& apk add \--no-cache \  
apache2 \  
apache2-utils \  
perl \  
perl-cgi \  
perl-dbd-mysql \  
perl-dbd-pg \  
perl-digest-md5 \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& cd /var/www \  
&& curl -L http://dbma.ca/DBMA_SQL_V${DBMA_VERSION}.tar -o
DBMA_SQL_V${DBMA_VERSION}.tar \  
&& echo -n "$DBMA_SHA256 DBMA_SQL_V${DBMA_VERSION}.tar" | sha256sum -c - \  
&& tar -xvf DBMA_SQL_V${DBMA_VERSION}.tar \  
&& rm -rf DBMA_SQL_V${DBMA_VERSION}.tar \  
&& chmod 755 /var/www/dbmailadministrator/*.cgi \  
  
&& mkdir -p /run/apache2 \  
&& mkdir -p /var/log/apache \  
&& ln -sf /proc/1/fd/1 /var/log/apache2/access.log \  
&& ln -sf /proc/1/fd/2 /var/log/apache2/error.log \  
  
&& apk del .build-deps  
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
COPY service.conf /etc/apache2/conf.d/service.conf  
COPY apache.hcl /etc/apache.hcl  
COPY DBMA_CONFIG.DB.template /root/DBMA_CONFIG.DB.template  
  
CMD ["/usr/local/bin/consul-template", "-config", "/etc/apache.hcl"]  

