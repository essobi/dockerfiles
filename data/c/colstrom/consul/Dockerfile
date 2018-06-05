FROM colstrom/alpine  
  
ENV CONSUL_VERSION 0.6.0  
ENV CONSUL_SHA256
307fa26ae32cb8732aed2b3320ed8daf02c28b50d952cbaae8faf67c79f78847  
  
RUN apk-install ca-certificates \  
&& wget -O /tmp/consul.zip
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
\  
&& echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& unzip /tmp/consul.zip -d /usr/local/bin/ \  
&& rm /tmp/consul.zip  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
ENTRYPOINT ["consul"]  

