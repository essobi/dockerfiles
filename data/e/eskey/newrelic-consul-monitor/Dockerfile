FROM java:7  
# Install monitor  
COPY . /usr/src/newrelic-consul-monitor  
RUN cd /opt && tar xvfz /usr/src/newrelic-consul-
monitor/dist/newrelic_consul_plugin-1.0.0.tar.gz  
WORKDIR /opt/newrelic_consul_plugin-1.0.0  
  
# Install consul-template  
ADD https://github.com/hashicorp/consul-
template/releases/download/v0.7.0/consul-template_0.7.0_linux_amd64.tar.gz
/tmp/consul-template.tar.gz  
RUN cd /tmp && tar xvfz /tmp/consul-template.tar.gz && mv consul-
template_0.7.0_linux_amd64/consul-template /bin/consul-template  
  
RUN mkdir /consul-template/  
RUN mv /usr/src/newrelic-consul-monitor/scripts/consul-template.sh /consul-
template/  
RUN chmod u+x /consul-template/*  
  
ENV CONSUL_CLUSTER consul.service.consul:8500  
ENV TEMPLATE_NR /usr/src/newrelic-consul-monitor/config/newrelic.json.ctmpl  
ENV TEMPLATE_PL /usr/src/newrelic-consul-monitor/config/plugin.json.ctmpl  
ENV COMMAND "java -jar /opt/newrelic_consul_plugin-1.0.0/plugin.jar"  
ENTRYPOINT ["/consul-template/consul-template.sh"]  

