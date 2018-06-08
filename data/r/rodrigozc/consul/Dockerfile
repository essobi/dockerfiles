FROM debian:stretch-slim  
  
LABEL author.name="Rodrigo Zampieri Castilho"  
LABEL author.email="rodrigo.zampieri@gmail.com"  
LABEL repository.url="https://bitbucket.org/rcastilho/consul"  
  
ENV DUMB_INIT_VERSION "1.2.0"  
ENV CONSUL_VERSION "1.0.2"  
ENV CONSUL_TEMPLATE_VERSION "0.19.4"  
ENV APPLICATION_DEFAULT_NAME "consul"  
ENV CONSUL_DEFAULT_SERVER "consul-server"  
ENV CONSUL_DEFAULT_INTERFACE "eth0"  
ENV CONSUL_DEFAULT_DATACENTER "dc1"  
ENV LOCALE_DEFAULT "en_US.UTF-8"  
ENV LOCALTIME_DEFAULT "UTC"  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends locales unzip wget ca-
certificates iproute2 telnet dnsutils inetutils-ping procps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/* \  
&& rm /etc/environment \  
# dumb-init Installation  
&& wget --no-check-certificate https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb \  
&& dpkg -i dumb-init_${DUMB_INIT_VERSION}_amd64.deb \  
&& rm dumb-init_${DUMB_INIT_VERSION}_amd64.deb \  
# Consul Installation  
&& mkdir -p /etc/consul \  
&& mkdir -p /var/consul \  
&& wget --no-check-certificate
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
\  
&& unzip consul_${CONSUL_VERSION}_linux_amd64.zip \  
&& mv consul /usr/sbin/consul \  
&& chmod +x /usr/sbin/consul \  
&& rm consul_${CONSUL_VERSION}_linux_amd64.zip \  
# Consul Template Installation  
&& mkdir -p /etc/consul-template/templates \  
&& wget --no-check-certificate https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& mv consul-template /usr/sbin/consul-template \  
&& chmod +x /usr/sbin/consul-template \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
WORKDIR /  
  
ADD consul-template/ /etc/consul-template/  
ADD run/ /docker/run/  
ADD config/ /config/  
ADD *.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

