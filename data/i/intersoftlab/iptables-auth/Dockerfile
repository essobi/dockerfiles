FROM debian  
  
ENV CONSUL_TPL_VERSION 0.15.0  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
unzip \  
iptables \  
python-pip \  
&& curl -sSL https://releases.hashicorp.com/consul-
template/${CONSUL_TPL_VERSION}/consul-
template_${CONSUL_TPL_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TPL_VERSION}_linux_amd64.zip \  
&& unzip consul-template_${CONSUL_TPL_VERSION}_linux_amd64.zip -d
/usr/local/bin \  
&& chmod +x /usr/local/bin/consul-template \  
&& rm consul-template_${CONSUL_TPL_VERSION}_linux_amd64.zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./ /  
RUN chmod +x /startup.sh  
RUN pip install -r /app/requirements.txt  
RUN mkdir -p /templates /data  
  
ENTRYPOINT ["/startup.sh"]

