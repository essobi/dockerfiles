FROM kibana:5.2.1  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
wget \  
unzip \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install consul-template  
ENV CONSUL_TEMPLATE_VERSION 0.16.0  
ENV CONSUL_TEMPLATE_SHA256
064b0b492bb7ca3663811d297436a4bbf3226de706d2b76adade7021cd22e156  
  
RUN wget -q -O /tmp/consul-template.zip https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo "${CONSUL_TEMPLATE_SHA256} /tmp/consul-template.zip" | sha256sum -c -
\  
&& gunzip -c /tmp/consul-template.zip > /usr/local/bin/consul-template \  
&& chmod +x /usr/local/bin/consul-template \  
&& rm /tmp/consul-template.zip  
  
RUN mkdir /srv/kibana && chown kibana:kibana /srv/kibana \  
&& ln -fs /srv/kibana/kibana.yml /etc/kibana/kibana.yml  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["consul-template", "-config=/srv/consul-template.cfg"]  
  
EXPOSE 5601  

