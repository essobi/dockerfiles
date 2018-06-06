FROM ubuntu:latest  
ENV HELM_VERSION=v2.9.1 UNITTEST_VERSION=v0.1.2  
RUN apt update && \  
apt install -y wget git curl && \  
wget -qO- https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xzv --strip-components=1 -C
/usr/local/bin/ && \  
helm init --client-only && \  
helm plugin install https://github.com/lrills/helm-unittest --version
${UNITTEST_VERSION}  
ENV https_proxy=http://proxy.evry.com:8080  

