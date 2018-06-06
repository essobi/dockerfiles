FROM alpine:latest  
  
ENV CONSUL_TEMPLATE_VERSION "0.18.5"  
ENV DOCKER_HOST "unix:///tmp/docker.sock"  
  
ENTRYPOINT [ "/usr/local/bin/consul-template" ]  
  
RUN apk -U add curl tar openssl && \  
wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -qO /tmp/consul-
template.zip && \  
unzip -d /usr/local/bin /tmp/consul-template.zip && \  
rm /tmp/consul-template.zip && \  
curl https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz -s | tar
-xzC /usr/bin --strip-components=1  

