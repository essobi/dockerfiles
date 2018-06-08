FROM solvebio/alpine-consul  
  
ENV CONSUL_VERSION=0.6.4  
ENV CONSUL_CONFIG_DIR=/etc/consul.d  
# Download and install Consul UI  
RUN apk add \--update curl && \  
curl -sSL -o /tmp/consul_web_ui.zip
https://releases.hashicorp.com/consul/{$CONSUL_VERSION}/consul_{$CONSUL_VERSION}_web_ui.zip
&& \  
mkdir /ui && \  
chown -R consul:consul /ui && \  
cd /ui && \  
cp /tmp/consul_web_ui.zip /ui/ && \  
unzip consul_web_ui.zip && \  
apk del \--purge curl && \  
rm -rf /var/cache/apk/* consul_web_ui.zip  
  
  
ADD root /  

