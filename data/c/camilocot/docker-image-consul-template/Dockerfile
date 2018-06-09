FROM gliderlabs/alpine  
  
ENV CONSUL_TEMPLATE_VERSION 0.16.0-rc1  
  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/  
  
RUN cd /tmp && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv consul-template /bin/consul-template && \  
rm -rf /tmp && \  
apk -U add bash && \  
apk -U add netcat-openbsd  
  
ADD send-container-signal.sh /  
RUN chmod +x /send-container-signal.sh  
  
ENTRYPOINT ["/bin/consul-template"]  

