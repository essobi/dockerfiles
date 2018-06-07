FROM haproxy:1.7  
RUN apt-get update && apt-get -y install curl rsyslog  
  
RUN mkdir -p /run/haproxy/  
RUN mkdir -p /var/lib/haproxy/  
COPY ./gen_haproxy_config.sh /  
COPY ./haproxy_template.cfg /  
  
ENV MESOS_DNS_IP_PORT http://127.0.0.1:8123  
ENV MESOS_DNS_SERVICES _rfp-db-rfp._tcp.marathon.mesos  
  
RUN chmod +x /gen_haproxy_config.sh  
  
EXPOSE 5432  
EXPOSE 1936  
ENTRYPOINT service rsyslog start && dash /gen_haproxy_config.sh
/haproxy_template.cfg /usr/local/etc/haproxy/haproxy.cfg ${MESOS_DNS_IP_PORT}
${MESOS_DNS_SERVICES} && /docker-entrypoint.sh haproxy -f
/usr/local/etc/haproxy/haproxy.cfg  

