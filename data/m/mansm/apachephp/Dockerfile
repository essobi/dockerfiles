FROM php:5.6-apache  
ENV CONSUL_AGENT_VERSION=0.6.0  
RUN apt-get update && apt-get install -y supervisor wget unzip && apt-get
clean  
  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /etc/consul.d  
RUN wget
https://releases.hashicorp.com/consul/${CONSUL_AGENT_VERSION}/consul_${CONSUL_AGENT_VERSION}_linux_amd64.zip
-O /tmp/consul-agent.zip && unzip /tmp/consul-agent.zip && mv consul
/usr/local/bin  
  
COPY src/ /var/www/html/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY web.json /etc/consul.d/web.json  
  
CMD ["/usr/bin/supervisord"]

