FROM haproxy:1.5.14  
ENV CT_VERSION 0.11.1  
RUN apt-get update && apt-get install -y unzip  
  
# Install consul-template  
ADD https://releases.hashicorp.com/consul-template/${CT_VERSION}/consul-
template_${CT_VERSION}_linux_amd64.zip consul-
template_${CT_VERSION}_linux_amd64.zip  
RUN unzip consul-template_${CT_VERSION}_linux_amd64.zip && rm -f consul-
template_${CT_VERSION}_linux_amd64.zip  
RUN mv consul-template /usr/bin/  
RUN chmod 555 /usr/bin/consul-template  
  
# Configure consul-template  
RUN mkdir -p /etc/consul-template  
VOLUME /etc/consul-template  
ADD consul-template.cfg /etc/consul-template/consul-template.cfg  
ADD haproxy.tmpl /etc/consul-template/haproxy.tmpl  
  
# Create volume for HAProxy config. Only really useful for
monitoring/debugging.  
RUN mkdir -p /etc/haproxy  
VOLUME /etc/haproxy  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/bin/consul-template"]  
  
CMD ["-config", "/etc/consul-template/consul-template.cfg"]  

