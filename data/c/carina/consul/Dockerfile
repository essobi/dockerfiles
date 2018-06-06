FROM busybox  
MAINTAINER murali.allada@rackspace.com  
  
ENV CONSUL_VERSION 0.6.1  
ENV CONSUL_SHA256
dbb3c348fdb7cdfc03e5617956b243c594a399733afee323e69ef664cdadb1ac  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
/tmp/consul.zip  
  
RUN echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& cd /bin \  
&& unzip /tmp/consul.zip \  
&& chmod +x /bin/consul \  
&& rm /tmp/consul.zip  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
/tmp/webui.zip  
RUN cd /tmp && mkdir /ui && unzip webui.zip -d /ui && rm webui.zip  
  
EXPOSE 8301 8301/udp 8302 8302/udp 8500  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

