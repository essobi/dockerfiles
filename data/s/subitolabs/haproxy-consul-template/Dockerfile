FROM haproxy:1.5  
MAINTAINER Subito Labs  
  
RUN apt-get update  
#RUNIT  
RUN \  
apt-get install --no-install-recommends -y runit &&\  
rm -rf /var/lib/apt/lists/*  
#CONSUL TEMPLATE  
RUN \  
apt-get update && apt-get install --no-install-recommends -y wget unzip && \  
wget --no-check-certificate https://releases.hashicorp.com/consul-
template/0.12.0/consul-template_0.12.0_linux_amd64.zip &&\  
unzip consul-template_0.12.0_linux_amd64.zip &&\  
rm -f consul-template_0.12.0_linux_amd64.zip &&\  
chmod +x consul-template &&\  
mv consul-template /bin/ &&\  
rm -rf /var/lib/apt/lists/*  
  
#QDISC  
RUN \  
apt-get update && apt-get install --no-install-recommends -y libnl-utils
iptables kmod && \  
rm -rf /var/lib/apt/lists/*  
  
COPY scripts/init/haproxy.sh /etc/service/haproxy/run  
COPY scripts/init/haproxy_reload.sh /usr/local/sbin/haproxy_reload  
  
RUN chmod +x /usr/local/sbin/haproxy_reload  
  
COPY scripts/init/consul_template.sh /etc/service/consul_template/run  
COPY scripts/init/runsvdir-start.sh /usr/local/sbin/runsvdir-start  
  
RUN chmod +x /etc/service/haproxy/run /etc/service/consul_template/run
/usr/local/sbin/runsvdir-start  
  
ENTRYPOINT ["/usr/local/sbin/runsvdir-start"]  

