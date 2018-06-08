FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
  
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip
/tmp/consul.zip  
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_web_ui.zip
/tmp/webui.zip  
  
ADD ./config /config/  
  
RUN apt-get -y update && \  
apt-get -y install unzip && \  
cd /bin && \  
unzip /tmp/consul.zip && \  
chmod +x /bin/consul && \  
rm /tmp/consul.zip && \  
cd /tmp && unzip webui.zip -d dist && mv dist /ui && rm webui.zip && \  
mkdir /data && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV DNS_RESOLVES consul  
ENV DNS_PORT 53  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
  
VOLUME ["/data", "/tmp"]  
  
ENTRYPOINT ["/bin/consul"]  
CMD ["agent", "-server", "-pid-file", "/tmp/consul.pid", "-config-dir",
"/config"]  

