FROM nexia/ubuntu  
MAINTAINER jgeiger@gmail.com  
  
EXPOSE 443 8080  
WORKDIR /tmp  
  
ENV CONSUL_TEMPLATE_VERSION=0.18.1  
USER root  
  
RUN add-apt-repository ppa:vbernat/haproxy-1.7 \  
&& apt-get -qq -y update \  
&& apt-get -qq -y install \  
haproxy \  
&& wget --quiet "https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" -O
/tmp/consul_template.zip \  
&& unzip /tmp/consul_template.zip \  
&& mv consul-template /usr/bin \  
&& apt-get -qq -y autoremove \  
&& apt-get -qq -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/config"]  
  
ENTRYPOINT [ "tini", "--" ]  
  
CMD [ "consul-template", "-config=/config/haproxy.json" ]  

