FROM jalaziz/base:alpine  
  
ENV CONSUL_TEMPLATE_VERSION 0.14.0  
RUN wget -q https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& mv consul-template /usr/local/bin \  
&& rm -f consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
VOLUME [ "/config", "/templates" ]  
  
ENTRYPOINT [ "/usr/local/bin/consul-template" ]  
CMD [ "-config=/config" ]  

