FROM haproxy  
  
ENV CONSUL_TEMPLATE_VERSION=0.11.1  
RUN apt-get update && apt-get install -y wget unzip && rm -rf
/var/lib/apt/lists/*  
  
RUN wget \  
\--no-check-certificate \  
-O "/tmp/consul-template.zip" \  
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& unzip -o /tmp/consul-template.zip -d /bin \  
&& rm /tmp/consul-template.zip  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 1936  
COPY haproxy.hcl /tmp/haproxy.hcl  
COPY haproxy.ctmpl /tmp/haproxy.ctmpl  
  
CMD ["consul-template", "-config=/tmp/haproxy.hcl"]  

