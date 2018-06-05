FROM haproxy:latest  
  
RUN apt-get update  
RUN apt-get install -y unzip iptables  
  
ENV CONSUL_TEMPLATE_VERSION=0.15.0  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /  
  
RUN unzip /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv /consul-template /usr/local/bin/consul-template && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
ADD haproxy.cfg.ctmpl /  
ADD run_haproxy.sh /  
ADD entrypoint.sh /  
  
ENV PORT 80  
ENV CONSUL 172.17.0.1:8500  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  

