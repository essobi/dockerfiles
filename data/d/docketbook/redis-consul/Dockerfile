FROM redis:3.2.1-alpine  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
make \  
openssl \  
unzip \  
curl \  
&& curl -k -L -o containerpilot.tar.gz
https://github.com/joyent/containerpilot/releases/download/2.4.3/containerpilot-2.4.3.tar.gz
\  
&& tar -xzf containerpilot.tar.gz -C /usr/local/bin \  
&& rm -r containerpilot.tar.gz \  
&& curl -k -L -o /tmp/consul.zip
https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& mkdir /config \  
&& mkdir /consul-data \  
&& apk del .build-deps  
  
COPY redis-consul.json /etc/redis-consul.json  
COPY redis.conf /usr/local/etc/redis/redis.conf  
ENV CONTAINERPILOT=file:///etc/redis-consul.json  
  
EXPOSE 6379  
ENTRYPOINT [ "/usr/local/bin/containerpilot", "redis-server",
"/usr/local/etc/redis/redis.conf"]

