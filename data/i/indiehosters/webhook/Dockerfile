FROM debian:jessie  
  
ENV WEBHOOK_VERSION 2.6.0  
ENV DOCKER_VERSION 1.11.2  
ENV COMPOSE_VERSION 1.9.0  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
gnupg2 \  
ssh && \  
apt-key adv \  
\--keyserver hkp://ha.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && apt-get install -y \--no-install-recommends \  
docker-engine=${DOCKER_VERSION}-0~jessie && \  
curl -fsSL -o webhook.tar.gz \  
"https://github.com/adnanh/webhook/releases/download/${WEBHOOK_VERSION}/webhook-
linux-amd64.tar.gz" && \  
tar -xzf webhook.tar.gz -C /tmp && \  
mv /tmp/webhook-linux-amd64/webhook /usr/local/bin && \  
curl -L
"https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-
compose-Linux-x86_64" > /usr/local/bin/docker-compose &&\  
chmod +x /usr/local/bin/docker-compose && \  
rm -rf webhook.tar.gz && \  
rm -rf /tmp/webhook-linux-amd64 && \  
rm -r /var/lib/apt/lists/*  
  
CMD webhook -hooks /hooks.json -verbose -port 80 -hotreload -urlprefix
XxosJDdRpo7Rww87VkJGzv1QLegnhh-uniq-libresh  

