### QNIBTerminal ubuntu image  
FROM qnib/u-syslog:14.04  
RUN apt-get update && \  
apt-get install -y bsdtar curl  
ENV TERM=xterm \  
CONSUL_VER=0.6.4 \  
BOOTSTRAP_CONSUL=false \  
RUN_SERVER=false \  
CT_VER=0.15.0 \  
DUMB_INIT_VER=1.1.1 \  
QNIB_CONSUL=0.1.3.4  
RUN apt-get update \  
&& apt-get install -y bsdtar curl wget \  
&& curl -fsL
https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip
| bsdtar xf - -C /usr/local/bin/ \  
&& chmod +x /usr/local/bin/consul \  
&& mkdir -p /opt/consul-web-ui/ \  
&& curl -fsL
https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_web_ui.zip
|bsdtar xf - -C /opt/consul-web-ui/ \  
&& unset CONSUL_VER \  
&& curl -Lsf https://releases.hashicorp.com/consul-template/${CT_VER}/consul-
template_${CT_VER}_linux_amd64.zip |bsdtar xf - -C /usr/local/bin/ \  
&& chmod +x /usr/local/bin/consul-template \  
&& unset CT_VER \  
&& mkdir -p /opt/qnib/ \  
&& curl -fsL https://github.com/qnib/consul-
content/releases/download/${QNIB_CONSUL}/consul.tar |tar xf - -C /opt/qnib/ \  
&& unset QNIB_CONSUL \  
&& wget -qO /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VER}/dumb-init_${DUMB_INIT_VER}_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
&& unset DUMB_INIT_VER  
  
ADD etc/consul.d/agent.json /etc/consul.d/  
ADD etc/supervisord.d/consul.ini /etc/supervisord.d/  

