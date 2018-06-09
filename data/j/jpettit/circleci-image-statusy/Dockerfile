FROM docker:latest  
  
ENV COMPOSE_VERSION 1.16.0-rc1  
  
RUN set -ex; \  
apk add \--no-cache --virtual .build-deps \  
python python3 git bash curl openssl; \  
\  
pip3 install docker-compose==$COMPOSE_VERSION; \  
\  
version=$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt); \  
curl -L https://storage.googleapis.com/kubernetes-
release/release/$version/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl; \  
chmod +x /usr/local/bin/kubectl; \  
\  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get |
bash; \  
curl -sSL https://sdk.cloud.google.com | bash;  
  

