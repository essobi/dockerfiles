FROM node:5-slim  
MAINTAINER Andrea Usuelli (andreausu@gmail.com)  
  
ADD . /usr/src/app  
  
RUN curl -L
https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-
amd64.tar.gz -o etcd-v2.2.2-linux-amd64.tar.gz && \  
tar xzvf etcd-v2.2.2-linux-amd64.tar.gz && \  
cd etcd-v2.2.2-linux-amd64 && \  
chmod +x etcdctl && \  
cp etcdctl /usr/bin && \  
cd .. && \  
rm -rf etcd-v2.2.2-linux-amd64* && \  
cd /usr/src/app && \  
npm install -g cloudflare-cli@1.5  
  
ENV CLOUDFLARE_TOKEN=token \  
CLOUDFLARE_EMAIL=user@example.com \  
CLOUDFLARE_DOMAIN=example.com \  
IP_ADDRESSES=127.0.0.1  
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]  

