FROM ubuntu:trusty  
MAINTAINER WOW! Group Development  
  
ADD https://github.com/krallin/tini/releases/download/v0.9.0/tini /tini  
RUN apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install apt-transport-https curl
unzip \  
&& curl -sSL https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install varnish \  
&& curl -sSL -o /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-
template/0.14.0/consul-template_0.14.0_linux_amd64.zip \  
&& unzip /tmp/cnsltmpl.zip -d /usr/local/bin \  
&& chmod +x /usr/local/bin/consul-template /tini \  
&& rm -f /etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get -y update \  
&& apt-get -y purge --auto-remove apt-transport-https curl unzip \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD runner reload /  
ADD default.vcl default.vcl.tmpl /etc/varnish/  
EXPOSE 8080  
ENTRYPOINT ["/tini", "--"]  
CMD ["/runner"]  

